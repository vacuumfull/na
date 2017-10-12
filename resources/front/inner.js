import Vue from 'vue';
import Dialog from './components/DialogComponent';
import LeftMenu from './components/LeftMenuComponent';
import Rate from './components/RateComponent';
import Comment from './components/CommentComponent';
import '../assets/css/cosmetic.css';
import '../assets/css/materialize.min.css';
import '../assets/css/style.css';

new Vue({
    el: '#inner',
    components: {
        'dialog-component': Dialog,
        'left-menu': LeftMenu,
        'rate-component': Rate,
        'comment-component': Comment
    }
})