import Vue from 'vue';
import $ from 'jquery';
import HelperMixin from './mixins/HelperMixin';
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
    mixins:[HelperMixin],
    data: {
        userInfo: {
            name: ""
        },
        messagesUnreadCount: {}
    },
    mounted(){
        $(".button-collapse").sideNav();
        this.initSignup()
    },
    methods: {
        initSignup(){
            if (window.location.search === "?isOwner=true"){
                setTimeout(()=>{
                    this.info('Если Вы действительно являетесь владелецем места,<br> зарегистрируйтесь как Представитель и напишите админу,<br> либо напишите нам на почту')
                }, 2000)  
            }
        },
        link(string){
            window.location = window.location.origin + string;
        },
        openModal(userInfo){
           this.userInfo = userInfo;
        },
        transportMessagesCount(messagesCount){
            this.messagesUnreadCount = messagesCount;
        },
        showHelpText(){
            
        }
        
    }
})