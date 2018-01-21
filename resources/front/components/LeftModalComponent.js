import Vue from 'vue';
import $ from 'jquery';
import template from '../../tmp/components/left-modal.html';
import Materialize from 'materialize-css';

const LeftModal = Vue.extend({
    template,
    props: ['user-info'],
    data(){
        return {
            message: '',
            getter: '',
        }
    },
    watch:{
        userInfo(val){
            if (val['name'] !== ''){
                this.getter = val['name'];
                this.openModal();
            }
        }
    },
    mounted(){
        $('#left_message_window').modal();
    },
    methods: {
        sendMessage(){
            let uri = '/api/1/message',
                self = this;
            if (self.message.length === 0){
                return;
            }
            $.post(uri, { message: self.message })
                .done((data) => {
                    self.successAction("Сообщение успешно отправлено!");
                    $('#left_message_window').modal('close');
                })
                .fail((error) => {
                    console.log(error);
                })
        },
        openModal(){
            $('#left_message_window').modal('open');
        },
        successAction(message){
            Materialize.toast(message, 4000);
        },
    }
})

export default LeftModal;
