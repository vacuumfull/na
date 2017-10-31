import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import LeftMessages from './components/LeftMessagesComponent';
import LeftModal from './components/LeftModalComponent';

new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'left-messages': LeftMessages,
        'left-modal': LeftModal,
    },
    data: {
        left: -5,
        userInfo: {
            name: ""
        },
        dialogInfo: {}
    },
    mounted(){
        $(".button-collapse").sideNav();
        $('select').material_select();
        $('.tooltipped').tooltip({delay: 50});
    },
    updated(){
        setTimeout(() => {
            let elem = document.getElementById('sidenav-overlay');
            if (elem !== null){
                elem.addEventListener('click', () => {
                    this.left = -5;
                })
            }
        }, 300);
    },
    methods: {
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
});
