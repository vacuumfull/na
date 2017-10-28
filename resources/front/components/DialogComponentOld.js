import Vue from 'vue';
import $ from 'jquery';
import _ from 'lodash';
import Messages from './MessagesComponent';
import Materialize from 'materialize-css';
import template from '../../tmp/components/dialog.html';

const Dialogold = Vue.extend({
    template,
    components: {
        messages: Messages
    },
    props: ['user-role', 'is-login'],
    data() {
        return {
            message: "",
            activeMessages: [],
            users: [],
            authors: {
                name: "",
                count: 0,
                messages: [],
            },
            senders: {},
            selectedGetter: "",
            showSenders: false,
            showGetterName: false,
            showScroll: false,
            filterAdmin: true,
            filterOrganizer: true,
            filterArtist: true,
            filterDeputy: true,
            filterUser: true,
            selectAll: false,
        }
    },
    created: function(){

        this.getUsers();
        this.$on('message', function(msg){
            console.log(msg)
            let authors = [];
            if (msg.length != undefined){
                this.senders = msg;
                this.senders.forEach(function(item, i, arr){
                    let name = item.author;
                    let count = 0;
                    let messages = [];
                    for (let j = 0; j < arr.length; j ++ ){
                        if (item.author.indexOf(arr[j].author) == 0){
                            let inner = {
                                content: arr[j].content,
                                time: arr[j].created_at
                            };
                            messages.push(inner);
                            count += 1;
                        }
                    }
                    let author = {
                        id: i,
                        name: name,
                        count: count,
                        messages: messages,
                    };
                    authors.push(author);
                });
                for (let i in authors) {
                    for (let j = 0; j < authors.length; j ++ ){
                        if (authors[i] != undefined){
                            if (authors[i].name.indexOf(authors[j].name) == 0 && i != j){
                                authors.splice(j, 1);
                            }
                        }
                    }
                }
                this.authors = authors;

                this.authors.forEach(function(item, i){
                    item.id = i;
                });
                this.showSenders = true;
            }

        });
    },
    methods: {
        openDialog(){
            $('#dialog_window').modal();
            $('#dialog_window').modal('open');

        },
        openMessages(id, author){
            let self = this,
                uri = '/messages/read';
            self.activeMessages = self.authors[id].messages;
            self.selectedGetter = author;
            self.showGetterName = true;
            $.post(uri, {
                    author: author
                }
            ).done(function(data){
                if (data.response > 0){
                    self.$emit('read');
                }
            })
                .fail(function(error) {
                    console.log(error);
                });
        },
        successAction(message){
            Materialize.toast(message, 4000);
        },
        checkHeight(classname){
            var field = document.querySelectorAll(classname)[0];
            var height = field.offsetHeight;
            return height;
        },
        getUsers(){
            let uri = "/user/users/advanced",
                self = this;

            $.get(uri,
                {
                    filterAdmin: self.filterAdmin,
                    filterOrganizer: self.filterOrganizer,
                    filterDeputy: self.filterDeputy,
                    filterArtist: self.filterArtist,
                    filterUser: self.filterUser
                })
                .done(function(data){
                    self.users =  data.response;
                    var height = self.checkHeight(".__usersfield");
                    if (height >  298){
                        self.showScroll = true;
                    }

                })
                .fail(function(error) {
                    console.log(error);
                });
        },
        selectGetter: function(name){
            let self = this;
            self.selectedGetter = name;
            self.showGetterName = true;
            document.querySelectorAll(".__dialog-field .materialize-textarea")[0].focus();

        },
        setForAll: function(){
            if (this.selectAll === true){
                this.showGetterName = true;
                this.selectedGetter = 'все';
                document.querySelectorAll(".__dialog-field .materialize-textarea")[0].focus();
            } else {
                this.showGetterName = false;
            }
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
                author = document.getElementById("username").innerText;

            if (self.selectAll === true){
                let uri = "/messages/massive",
                    users = [];

                self.users.forEach(function(item){
                    users.push(item.name);
                });
                $.post(uri, {
                    author: author,
                    getter: JSON.stringify(users),
                    content: self.message + document.getElementById("img-field").innerHTML,
                })
                    .done(function(data){
                        self.message = "";
                        document.querySelectorAll(".__dialog-field label")[0].className = "";
                        self.successAction("Успешно отправлено!");
                    })
                    .fail(function(error) {
                        console.log(error);
                    });

            } else {

                let uri = "/messages/create";
                $.post(uri, {
                    author: author,
                    getter: self.selectedGetter,
                    content: self.message + document.getElementById("img-field").innerHTML,
                })
                    .done(function(data){
                        self.message = "";
                        document.querySelectorAll(".__dialog-field label")[0].className = "";
                        self.successAction("Успешно отправлено!");
                    })
                    .fail(function(error) {
                        console.log(error);
                    });
            }
        },
        closeModal(){
            $('#dialog_window').modal('close');
        }
    }
});

export default Dialogold;
