import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import LeftMessages from './components/LeftMessagesComponent';
import LeftModal from './components/LeftModalComponent';
import MapComponent from './components/MapComponent';


new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'left-messages': LeftMessages,
        'left-modal': LeftModal,
        'map-component': MapComponent,
    },
    data: {
        left: -5,
        userInfo: {
            name: ""
        },
        showModal:  false,
        showMap: false,
        dialogInfo: {}
    },
    mounted(){
        $(".button-collapse").sideNav();
        $('select').material_select();
        $('.tooltipped').tooltip({delay: 50});
        setTimeout(() => {
            let mapInput = document.querySelectorAll('#map-coordinates > div > input')[0];
            mapInput.addEventListener('click', () => {
                this.showModal = !this.showModal;
                this.showMap = true;
            })
        }, 200);
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
        },
        setCoordinates(coordinates){
            document.querySelectorAll('#map-coordinates > div > input')[0].value = coordinates;
        }
    }
});
