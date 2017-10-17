import Vue from 'vue';
import Dialog from './components/DialogComponent';
import LeftMenu from './components/LeftMenuComponent';
import Rate from './components/RateComponent';
import Comment from './components/CommentComponent';

new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'left-menu': LeftMenu,
        'rate-component': Rate,
        'comment-component': Comment
    }
})