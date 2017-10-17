import Vue from 'vue';
import Search from './components/SearchComponent';
import Dialog from './components/DialogComponent';
import LeftMenu from './components/LeftMenuComponent';

new Vue({
    el: '#index',
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
