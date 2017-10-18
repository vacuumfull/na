import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';

new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
    }, 
    mounted(){
        $('select').material_select();
        $('.tooltipped').tooltip({delay: 50});
    },
    methods: {
        
    }
});