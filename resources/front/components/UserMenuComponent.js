import Vue from 'vue';
import $ from 'jquery';
import Materialize from 'materialize-css';
import template from '../../tmp/components/user-menu.html';

const UserMenu = Vue.extend({
    template,
    data() {
        return {
            left: -5,
            unread: 3,
            messagesUnread: [ 
            {
                name: 'Nikolas',
                role: 'organizer',
                avatar: '/src/reacl.jpg',
                messages: [
                    {
                        date: '11/11/2013',
                        text: 'hihihihi hello'
                    },
                    {
                        date: '11/12/2013',
                        text: 'Здорово нигеры!'
                    }
                ]
            },
            {
                name: 'Ann',
                role: 'deputy',
                avatar: null,
                messages: [
                    {
                        date: '13/10/2013',
                        text: 'hihihihi hello'
                    },
                    {
                        date: '11/09/2013',
                        text: 'Здорово нигеры!'
                    },
                    {
                        date: '11/11/2013',
                        text: 'HI BITCHES!'
                    }
                ]
            },
            ]
        }
    },
    mounted(){
        this.getMessages()
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
        getMessages(){
            this.transportMessages();
            return this.messagesUnread;
        },
        openDialog(){
            $('#dialog_window').modal('open');
        },
        move(){
            if (this.left === -5){
                this.left = 300;

            } else {
                this.left = -5;
            }
        },
        transportMessages(){
            this.$emit('transport-messages', this.messagesUnread);
        }
    }
});

export default UserMenu;