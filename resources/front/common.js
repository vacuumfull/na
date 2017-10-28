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
    data: {
        left: -5
    },
    mounted(){
        $('#left_message_window').modal();
        $(".button-collapse").sideNav();
    },
    updated(){
        let elem = document.getElementById('sidenav-overlay');
        if (elem !== null){
            elem.addEventListener('click', () =>{
               this.left = -5;
            })
        }
    },
    methods: {
        link(string){
            window.location = window.location.origin + string;
        },
        openMenu(){
            if (this.left == -5){
                this.left = 300;
            } else {
                this.left = -5;
            }
        }
    }
})