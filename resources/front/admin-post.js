import Vue from 'vue';
import $ from 'jquery';
import Dialog from './components/DialogComponent';

new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
    }, 
    data:{

    },
    mounted(){
        $('select').material_select();
        $('.tooltipped').tooltip({delay: 50});
        $('#left_message_window').modal();
        $(".button-collapse").sideNav();
    },    
    methods: {
        
    }
});
