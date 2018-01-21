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
    data: {
        left: -5
    },
    mounted(){
        $('#left_message_window').modal();
        $(".button-collapse").sideNav();
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
        link(string){
            window.location = window.location.origin + string;
        },
        openMenu(){
            if (this.left === -5){
                this.left = 300;
            } else {
                this.left = -5;
            }
        }
    }
});
