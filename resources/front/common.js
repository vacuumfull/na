import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import '../assets/css/cosmetic.css';
import '../assets/css/materialize.min.css';
import '../assets/css/style.css';

new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
    },
    mounted(){
        $('#left_message_window').modal();
        $(".button-collapse").sideNav();
    },
    methods: {
        link(string){
            window.location = window.location.origin + string;
        }
    }
})