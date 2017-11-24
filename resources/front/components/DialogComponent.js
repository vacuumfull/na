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
            selected: null,
            users: [],
            messages: [],
            dialogId: 0
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
        },
        openDialog(){
            $('#dialog_window').modal('open');
        },
        openMessages(author){
            this.selected = author.messages;
            this.getter = author.name;
            this.isSelected = true;
        },
        getUnreadMessages(){
            let self = this,
                session = self.getSess(),
                uri = `/api/1/messages/unread/${session}`;
            $.get(uri)
                .done(data => {
                    if (data.error){
                        return console.error(data.error)
                    }
                    console.log(data)
                    data.map((item, key) => {
                        console.log(item)
                    })
                })
                .fail(error => {
                    console.error(error)
                })

            self.$emit('transport-count', 3)
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
                        console.error(data.error)
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
            let self = this,
                uri = '/api/1/message/',
                params = {
                    sessionid: self.getSess(),
                    content: self.message,
                    login: 'almamater',
                    dialog: self.dialogId
                }
            if (self.getter === null){
                return self.successAction('Выберите получателя!')
            }
            $.post(uri, params).done((data) => {
                if (data.success){
                    self.message = "";
                    self.successAction('Сообщение отправлено!')
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
