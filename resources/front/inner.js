import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import LeftMessages from './components/LeftMessagesComponent';
import LeftModal from './components/LeftModalComponent';
import UserMenu from './components/UserMenuComponent';
import Rate from './components/RateComponent';
import Comment from './components/CommentComponent';

new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'left-messages': LeftMessages,
        'left-modal': LeftModal,
        'rate-component': Rate,
        'user-menu': UserMenu,
        'comment-component': Comment
    },
    data: {
        left: -5,
        userInfo: {
            name: ""
        },
        dialogInfo: {},
        messagesUnread: {},
    },
    mounted(){
        $(".button-collapse").sideNav();
    },
    methods:{
        openModal(userInfo){
            this.userInfo = userInfo;
        },
        openDialog(){
            $('#dialog_window').modal('open');
        },
        transportUserMessages(messagesUnread){
            this.messagesUnread = messagesUnread;
        }
    }
})