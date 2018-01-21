import Vue from 'vue';
import Datepicker from 'vuejs-datepicker';
import moment from 'moment';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import LeftMessages from './components/LeftMessagesComponent';
import LeftModal from './components/LeftModalComponent';
import UserMenu from './components/UserMenuComponent';
import MapComponent from './components/MapComponent';
import TagsComponent from './components/TagsComponent';
import Settings from './components/SettingsComponent';


new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'left-messages': LeftMessages,
        'left-modal': LeftModal,
        'map-component': MapComponent,
        'tags-component': TagsComponent,
        'user-menu': UserMenu,
        'datepicker': Datepicker,
        'settings': Settings
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
            let mapInput = document.getElementById('id_coordinates');
            if (mapInput !== undefined && mapInput !== null){
                mapInput.addEventListener('click', () => {
                    this.showModal = !this.showModal;
                    this.showMap = true;
                })
            }
        }, 200);
    },
    methods: {
        init(){
            let currLocation = window.location.href;
            $(".button-collapse").sideNav();
            $('select').material_select();
            $('.tooltipped').tooltip({delay: 50});
            $('#id_annotation').addClass('materialize-textarea');
            $('#id_description').addClass('materialize-textarea');
            $('.__worktime textarea').addClass('materialize-textarea');
            $('.__playlist_content textarea').addClass('materialize-textarea');
            $('.__playlist_content label').text('Вставьте код с soundcloud или youtube');
            $('.__remove-field label').text('Удалить место');
            $('#modal-music').modal();
            if (currLocation.includes('/edit/')){
				this.setEditDate()
			}
        },
        customFormatter(date) {
            
            return;
        },
        setEditDate(){
            let input =  document.getElementById('id_date');
            if (input !== undefined && input !== null){
                this.date = input.value
            }
        },
        openModal(userInfo){
            this.userInfo = userInfo;
        },
        openDialog(){
            $('#dialog_window').modal('open');
        },
        setCoordinates(coordinates){
            document.getElementById('id_coordinates').value = coordinates;
        },
        transportMessagesCount(messagesCount){
            this.messagesUnreadCount = messagesCount;
        },
        setDate(date){
            let input = document.getElementById('id_date')
            if (input !== undefined && input !== null){
                this.date = moment(date).format('YYYY-MM-D')
                input.value = this.date;
            }
        },
        sendTelegramInfo(){
            let uri = `/api/1/telegram/info/`,
                info = "";

            if (window.location.href.includes('/blogs/')){
                info = document.getElementById('id_annotation').value;
            } else {
                info = document.getElementById('id_description').value;
            }

            $.post(uri, {info: info})
                .done(data => {
                   
                })
                .fail(error => {
                    console.error(error)
                })
        },
        sendTelegramLink(){
            let uri = `/api/1/telegram/link/`,
                link = window.location.pathname.replace("edit/", "");        

            $.post(uri, {link: link})
                .done(data => {
                   
                })
                .fail(error => {
                    console.error(error)
                })
        }

    }
});
