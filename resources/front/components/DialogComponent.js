import Vue from 'vue';
import $ from 'jquery';
import _ from 'lodash';
import Materialize from 'materialize-css';
import Storage from '../mixins/StorageMixin';
import Helper from '../mixins/HelperMixin';
import template from '../../tmp/components/dialog.html';

const Dialog = Vue.extend({
    template,
    props: ['user-role'],
    mixins: [Storage, Helper],
    data() {
        return {
            message: "",
            username: "",
            getter: null,
            isSelected: false,
            selectedMessages: [],
            unreadMessages: {},
            historyMessages: [],
            users: [{unread: [], username: ""}],
            openedDialog: {messages: [], open: false, dialog_id: 0, username: '', unread:[]},
            dialogs: [],
            dialogId: 0,
        }
    },
    mounted(){
        this.init()
    },
    methods: {
        init(){
            $('select').material_select();
            $('#dialog_window').modal();
            this.triggerGetUsers();
            this.getUserDialogs();
            this.username = document.getElementById('username').innerText;
        },
        openDialog(){
            $('#dialog_window').modal('open');
        },
        getHistory(username, offset, dialogId){
            let self = this,
                session = self.getSess(),
                uri = `/api/1/messages/history/${dialogId}/${session}/${offset}`;
            $.get(uri).done(data => {
                    if(data.error){
                        return console.error(data.error)
                    }
                   self.formatHistory(username, data, offset);
                   self.selectedMessages = [];
                   self.historyMessages.map(item => {
                       if (item.username === username && item.count > 0) {
                           item.show = true;
                       } else{
                           item.show = false;
                       }
                   })
                   console.log(data)
                })
                .fail(error => {
                    console.error(error)
                })
        },
        formatHistory(username, info, offset=0){
 
        },
       
        getUserDialogs(){
            let self = this,
                session = self.getSess(),
                uri = `/api/1/messages/dialogs/${session}`;
            $.get(uri).done(data => {
                    if(data.error){
                        return console.error(data.error)
                    }
                    self.dialogs = data;
                    _.each(self.users, item => {
                        self.setDialogsToUsers(item)
                    })
                }).fail(error => {
                    console.error(error)
                })
        },
        setDialogsToUsers(user){
            let self = this,
                countUnread = 0,
                dialogs = [];
                dialogs = self.dialogs.filter(item => {
                    if(self.username !== user.username) {
                        return item.from_user === user.username || item.to_user === user.username;   
                    } else {
                       return item.to_user === item.from_user && item.to_user === user.username && item.read;
                    } 
                })
                dialogs = _.uniqBy(dialogs, 'created_at') 
                self.users.map(item => {
                    if (item.username === user.username) {
                        item.messages = dialogs; item.open = false; 
                        item.unread = item.messages.length > 0 ? self.dialogs.filter(item => !item.read && self.username === item.to_user && item.to_user !== item.from_user) : [];
                        item.dialog_id = item.messages.length === 0 ? 0 : item.messages[0].dialog_id
                        if (item.unread.length === 0) {
    
                            item.unread = self.dialogs.filter(item => item.to_user === item.from_user && item.to_user === user.username && !item.read)
                            item.unread = _.uniqBy(item.unread, 'dialog_id') 
                            if (item.unread.length > 0){
                                item.messages = item.unread;
                                item.dialog_id = item.unread[0].dialog_id
                            } 
                        }

                        if (item.unread.length > 0) ++countUnread;
                    }
                })
                if (countUnread > 0)  self.$emit('transport-count', countUnread);
                console.log(self.users)
                
        },
        openUserDialog(user){
            this.users.map(item => {
                item.open = false;
                if (item.username === user.username){
                    if (item.unread.length > 0) this.readMessages(user)
                    item.open = true;
                    this.openedDialog = item;
                    this.isSelected = true;
                    this.getter = user.username;
                    this.dialogId = item.dialog_id;
                }
            });
        },
        readMessages(user){
            console.log(user)
            let self = this,
                countUnread = 0,
                uri = '/api/1/messages/read/',
                session = self.getSess(),
                params = {
                    dialog: user.dialog_id,
                    sessionid: session
                };
               
            $.post(uri, params).done(data => {
                if (data.success){
                    self.users.map(item => {
                        if (item.username === user.username) item.unread = [];
                        if (item.unread.length > 0) ++countUnread;
                    })
                    self.$emit('transport-count', countUnread)
                }
                if (data.error){
                    return console.error(data.error)
                }
            }).fail(error => {
                console.error(error)
            })
        },
        successAction(message){
            Materialize.toast(message, 4000);
        },
        triggerGetUsers(){
            this.users = this.storageGet('users') !== null ? this.storageGet('users') : false;
            if (!this.users) this.getUsers(); 
        },
        getUsers(){
            let self = this,
                session = self.getSess(),
                uri = `/api/1/users/${session}`;
            $.get(uri)
                .done(data => {
                    if (data.error){
                        return console.error(data.error)
                    }
                    self.users = data;
                })
                .fail(error => { 
                    console.error(error);
                });
        },
        selectGetter(name){
            document.querySelectorAll(".__dialog-field .materialize-textarea")[0].focus();
        },
        search(event){
            let self = this,
                keyword = event.target.value,
                users = self.storageGet('users');
            if (keyword.length <= 2) return self.users = self.storageGet('users');;
            self.users = users.filter((item) => {
                return item.username.indexOf(keyword) === 0;
            })
        },
        encodeImageFileAsURL(event) {
            let filesSelected = event.target.files;
            if (filesSelected.length > 0) {
                let fileToLoad = filesSelected[0];
                let fileReader = new FileReader();

                fileReader.onload = function(fileLoadedEvent) {
                    let srcData = fileLoadedEvent.target.result; // <--- data: base64
                    let newImage = document.createElement('img');
                    newImage.src = srcData;
                    newImage.className = "responsive-img";
                    document.getElementById("img-field").innerHTML = newImage.outerHTML;
                }
                fileReader.readAsDataURL(fileToLoad);
            }
        },
        getSess(){
            return document.getElementById('session_id').innerHTML;
        },  
        sendMessage(){
            let self = this,
                uri = '/api/1/message/',
                content = self.message + document.getElementById("img-field").innerHTML,
                params = {
                    sessionid: self.getSess(),
                    content: content,
                    login: self.getter,
                    dialog: self.dialogId
                }
            console.dir(params)
            if (self.getter === null){
                return self.successAction('Выберите получателя!')
            }
            
            $.post(uri, params).done((data) => {
                console.log(data)
                if (data.success){
                    self.message = "";
                    self.successAction('Сообщение отправлено!')
                    document.getElementById("img-field").innerHTML = "";
                }
                //if (data.info.length > 0) {
                //    self.dialogs.push(data.info)
                //}
                if (data.error){
                    console.error(data.error)
                }
            }).fail((error) => {
                console.error(error);
            });
        },
        closeModal(){
            $('#dialog_window').modal('close');
        }
    }
});

export default Dialog;
