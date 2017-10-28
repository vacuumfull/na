import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import LeftMessages from './components/LeftMessagesComponent';
import LeftModal from './components/LeftModalComponent';
import '../assets/css/cosmetic.css';
import '../assets/css/materialize.min.css';
import '../assets/css/style.css';


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
    },
    updated(){
        let elem = document.getElementById('sidenav-overlay');
        if (elem !== null){
            elem.addEventListener('click', () => {
               this.left = -5;
            })
        }
    },
    methods: {
        link(string){
            window.location = window.location.origin + string;
        },
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