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
            users: [
                {
                    name: "Vasya",
                    role: "deputy"
                },
                {
                    name: "Kyle",
                    role: "musician"
                },
                {
                    name: "Fedor",
                    role: "musician"
                },
                {
                    name: "Bondarchuk",
                    role: "organizer"
                },
                {
                    name: "Alice",
                    role: "admin"
                },
            ],
            senders: [
                {
                    name: 'Nikolas',
                    role: 'organizer',
                    avatar: '/src/reacl.jpg',
                    messages: [
                        {
                            date: '11/11/2013',
                            text: 'hihihihi hello'
                        },
                        {
                            date: '11/12/2013',
                            text: 'Здорово нигеры!'
                        }
                    ]
                },
                {
                    name: 'Ann',
                    role: 'deputy',
                    avatar: null,
                    messages: [
                        {
                            date: '13/10/2013',
                            text: 'hihihihi hello'
                        },
                        {
                            date: '11/09/2013',
                            text: 'Здорово нигеры!'
                        },
                        {
                            date: '11/11/2013',
                            text: 'HI BITCHES!'
                        }
                    ]
                }
            ]
        }
    },
    mounted(){
        $('select').material_select();
        $('#dialog_window').modal();
    },
    methods: {
        openDialog(){
            $('#dialog_window').modal('open');
        },
        openMessages(author){
            this.selected = author.messages;
            this.getter = author.name;
            this.isSelected = true;
        },
        successAction(message){
            Materialize.toast(message, 4000);
        },
        getUsers(){
            let uri = "/api/1/users",
                self = this;
            $.get(uri)
                .done(function(data){
                    self.users =  data.response;
                    self.storageSave('users', self.users);
                })
                .fail(function(error) {
                    console.log(error);
                });
        },
        selectGetter(name){
            document.querySelectorAll(".__dialog-field .materialize-textarea")[0].focus();
        },
        search(event){

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
        sendMessage(){
            let self = this,
                uri = '/api/1/message',
                params = {
                    getter: self.getter,
                    message: self.message
                }
            if (self.getter === null){
                return self.successAction('Выберите получателя!')
            }
            $.post(uri, params).done((data) => {

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
