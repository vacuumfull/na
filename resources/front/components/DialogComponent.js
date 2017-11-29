import Vue from 'vue';
import $ from 'jquery';
import _ from 'lodash';
import Materialize from 'materialize-css';
import Storage from '../mixins/StorageMixin';
import template from '../../tmp/components/dialog.html';

const Dialog = Vue.extend({
    template,
    props: ['user-role'],
    mixins: [Storage],
    data() {
        return {
            message: "",
            getter: null,
            isSelected: false,
            selectedMessages: [],
            unreadMessages: {},
            historyMessages: [],
            users: [],
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
            this.getUnreadMessages();
            this.getUserDialogs();
        },
        openDialog(){
            $('#dialog_window').modal('open');
        },
        formatDate(string){
            let date = new Date(string),
                hour = date.getHours(),
                minutes = date.getMinutes(),
                day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate(),
                month = date.getMonth() + 1,
                year = date.getFullYear();
            return `${day}/${month}/${year} ${hour}:${minutes}`;
        },
        getHistory(offset, dialogId){
            let self = this,
                session = self.getSess(),
                uri = `/api/1/messages/history/${dialogId}/${session}/${offset}`;
            $.get(uri).done(data => {
                    if(data.error){
                        return console.error(data.error)
                    }
                    console.log(data)
                })
                .fail(error => {
                    console.error(error)
                })
        },
        readMessages(messages, name){
            let self = this,
                uri = '/api/1/messages/read/',
                session = self.getSess(),
                dialog = self.dialogs.filter(item => item.username === name).reduce((sum,item) => item.dialog_id, 0),
                params = {
                    dialog: dialog,
                    sessionid: session
                };
            self.selectedMessages = messages;
            self.getter = name;
            self.isSelected = true;
            
            $.post(uri, params).done(data => {
                if (data.success){
                    delete self.unreadMessages[name];
                    self.$emit('transport-count', Object.keys(self.unreadMessages).length)
                }
                if (data.error){
                    return console.error(data.error)
                }
            }).fail(error => {
                console.error(error)
            })
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
                }).fail(error => {
                    console.error(error)
                })
        },  
        getUnreadMessages(){
            let self = this,
                session = self.getSess(),
                uri = `/api/1/messages/unread/${session}`;
            $.get(uri).done(data => {
                    if (data.error){
                        return console.error(data.error)
                    }
                    self.unreadMessages = _.groupBy(data, 'from_user')
                    self.$emit('transport-count', Object.keys(self.unreadMessages).length)
                })
                .fail(error => {
                    console.error(error)
                })
        },
        setGetter(name){
            let self = this;
            self.getter = name;
            self.isSelected = true;
            self.checkGetter(name);
        },
        checkGetter(name){
            let self = this;
            self.dialogId = 0;
            _.each(self.dialogs, (item) => { 
                if (_.includes(item, name)) self.dialogId = item.dialog_id;
                self.getHistory(0, item.dialog_id);
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
            if (keyword.length <= 2) return;
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
            this.checkGetter(this.getter)

            let self = this,
                uri = '/api/1/message/',
                content = self.message + document.getElementById("img-field").innerHTML,
                params = {
                    sessionid: self.getSess(),
                    content: content,
                    login: self.getter,
                    dialog: self.dialogId
                }

            if (self.getter === null){
                return self.successAction('Выберите получателя!')
            }
            
            $.post(uri, params).done((data) => {
                if (data.success){
                    self.message = "";
                    self.successAction('Сообщение отправлено!')
                    document.getElementById("img-field").innerHTML = "";
                }
                if (data.info.length > 0) {
                    self.dialogs.push(data.info)
                }
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
