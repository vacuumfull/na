import Vue from 'vue';
import Search from './components/SearchComponent';
import Dialog from './components/DialogComponent';
import LeftMenu from './components/LeftMenuComponent';
import '../assets/css/cosmetic.css';
import '../assets/css/materialize.min.css';
import '../assets/css/style.css';

new Vue({
    el: '#main',
    components: {
        'search-component': Search,
        'dialog-component': Dialog,
        'left-menu': LeftMenu
    },
    methods: {
        link(string){
            window.location = window.location.origin + string;
        }
    }
});
