import Vue from 'vue';
import Datepicker from 'vuejs-datepicker';
import moment from 'moment';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import LeftMessages from './components/LeftMessagesComponent';
import LeftModal from './components/LeftModalComponent';
import UserMenu from './components/UserMenuComponent';
import MapComponent from './components/MapComponent';



new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'left-messages': LeftMessages,
        'left-modal': LeftModal,
        'map-component': MapComponent,
        'user-menu': UserMenu,
        'datepicker': Datepicker
    },
    data: {
        userInfo: {
            name: ""
        },
        showModal:  false,
        showMap: false,
        date: null,
        messagesUnreadCount: 0,
    },
    mounted(){
        this.init()
        setTimeout(() => {
            let mapInput = document.querySelectorAll('#map-coordinates > div > div > input')[0];
            if (mapInput !== undefined){
                mapInput.addEventListener('click', () => {
                    this.showModal = !this.showModal;
                    this.showMap = true;
                })
            }
        }, 200);
    },
    methods: {
        init(){
            $(".button-collapse").sideNav();
            $('select').material_select();
            $('.tooltipped').tooltip({delay: 50});
            $('#id_annotation').addClass('materialize-textarea');
            $('#id_description').addClass('materialize-textarea');
            $('.__worktime textarea').addClass('materialize-textarea');
            $('.__remove-field label').text('Удалить место');
        },
        customFormatter(date) {
            
            return;
        },
        openModal(userInfo){
            this.userInfo = userInfo;
        },
        openDialog(){
            $('#dialog_window').modal('open');
        },
        setCoordinates(coordinates){
            document.querySelectorAll('#map-coordinates > div > div > input')[0].value = coordinates;
        },
        transportMessagesCount(messagesCount){
            this.messagesUnreadCount = messagesCount;
        },
        setDate(date){
            this.date = moment(date).format('YYYY-MM-D')
            document.getElementById('id_date').value = this.date;
        }
    }
});
