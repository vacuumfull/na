import Vue from 'vue';
import $ from 'jquery';
import Search from './components/SearchComponent';
import Dialog from './components/DialogComponent';

new Vue({
    el: '#index',
    components: {
        'search-component': Search,
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
});
