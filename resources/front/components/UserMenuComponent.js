import Vue from 'vue';
import $ from 'jquery';
import Materialize from 'materialize-css';
import template from '../../tmp/components/user-menu.html';

const UserMenu = Vue.extend({
    template,
    props: ['messages-unread-count'],
    data() {
        return {
            left: -5
        }
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
        openDialog(){
            $('#dialog_window').modal('open');
        },
        move(){
            if (this.left === -5){
                this.left = 300;

            } else {
                this.left = -5;
            }
        }
    }
});

export default UserMenu;