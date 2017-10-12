import Vue from 'vue';
import $ from 'jquery';
import template from '../../tmp/components/messages.html';
import Dialog from './DialogComponent';

const Messages = Vue.extend({
    data() {
        return {
            newMessages: 0,
            showMessagesCount: false,
            message: {}
        }
    },
    render(h){
        return template
    },
    created: function(){
        this.getUnreadMessages();
      //  Dialog.$on('read', function(){
      //      self.getUnreadMessages();
      //  })
    },
    updated(){

    },
    methods: {
        dialog: function(){
            this.$emit('dialog');
            this.$emit('message', this.message);
        },
        getUnreadMessages(){
            let uri = "/user/messages",
                self = this;

            $.get(uri)
                .done(function(data){
                    if (data.response.length > 0){
                        self.message = data.response;
                        self.newMessages = data.response.length;
                        self.showMessagesCount = true;
                    } else {
                        self.newMessages = 0;
                        self.showMessagesCount = false;
                    }
                })
                .fail(function(error) {
                    console.log(error);
                });
        }
    }
})

export default Messages
