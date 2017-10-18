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
    mounted(){
        $('#left_message_window').modal();
        $(".button-collapse").sideNav();
    },
})