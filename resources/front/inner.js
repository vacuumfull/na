import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';
import Rate from './components/RateComponent';
import Comment from './components/CommentComponent';

new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'rate-component': Rate,
        'comment-component': Comment
    },
    data: {
        left: -5
    },
    updated(){
        let elem = document.getElementById('sidenav-overlay');
        if (elem !== null){
            elem.addEventListener('click', () =>{
                this.left = -5;
            })
        }
    },
    mounted(){
        $('#left_message_window').modal();
        $(".button-collapse").sideNav();
    },
    methods:{
        openMenu(){
            if (this.left == -5){
                this.left = 300;
            } else {
                this.left = -5;
            }
        }
    }
})