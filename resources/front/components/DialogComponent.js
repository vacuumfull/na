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
            isSelected: false,
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
        $('#dialog_window').modal();
    },
    methods: {
        openDialog(){
            $('#dialog_window').modal('open');
        },
        openMessages(author){

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
        selectGetter: function(name){
            document.querySelectorAll(".__dialog-field .materialize-textarea")[0].focus();
        },
        setForAll: function(){

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

        },
        closeModal(){
            $('#dialog_window').modal('close');
        }
    }
});

export default Dialog;
