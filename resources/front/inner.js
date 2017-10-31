import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import LeftMessages from './components/LeftMessagesComponent';
import LeftModal from './components/LeftModalComponent';
import Rate from './components/RateComponent';
import Comment from './components/CommentComponent';

new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'left-messages': LeftMessages,
        'left-modal': LeftModal,
        'rate-component': Rate,
        'comment-component': Comment
    },
    data: {
        left: -5,
        userInfo: {
            name: ""
        },
        dialogInfo: {}
    },
    updated(){
        let elem = document.getElementById('sidenav-overlay');
        if (elem !== null){
            elem.addEventListener('click', () =>{
                this.left = -5;
            })
        }
    },
    mounted(){
        $(".button-collapse").sideNav();
    },
    methods:{
        move(){
            if (this.left == -5){
                this.left = 300;
            } else {
                this.left = -5;
            }
        },
        openModal(userInfo){
            this.userInfo = userInfo;
        },
        openDialog(){
            $('#dialog_window').modal('open');
        }
    }
})