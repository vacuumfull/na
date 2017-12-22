import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import LeftMessages from './components/LeftMessagesComponent';
import LeftModal from './components/LeftModalComponent';
import UserMenu from './components/UserMenuComponent';
import UserItems from './components/UserItemsComponent';
import Search from './components/SearchComponent';
import '../assets/css/cosmetic.css';
import '../assets/css/materialize.min.css';
import '../assets/css/style.css';


new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'left-messages': LeftMessages,
        'left-modal': LeftModal,
        'user-menu': UserMenu,
        'user-items': UserItems,
        'search': Search
    },
    data: {
        userInfo: {
            name: ""
        },
        messagesUnreadCount: {}
    },
    mounted(){
        $(".button-collapse").sideNav();
    },
    methods: {
        link(string){
            window.location = window.location.origin + string;
        },
        openModal(userInfo){
           this.userInfo = userInfo;
        },
        transportMessagesCount(messagesCount){
            this.messagesUnreadCount = messagesCount;
        }
        
    }
})