import Vue from 'vue';
import $ from 'jquery';
import template from '../../tmp/components/comments.html';
import Materialize from 'materialize-css';

const Comment = Vue.extend({
    template,
    props: [ 'isLogin',  'type', 'unique'],
    data(){
        return {
            content: "",
            offset: 0,
            comments: [],
        }
    },
    created(){
        this.getComments()
    },
    methods: {
        create(){
            let self = this,
                params = {
                    content: self.content
                },
                uri = '/api/1/comment/' + self.type + '/' + self.unique + '/' + this.getSess() + '/';
            self.content = self.content.replace(/^\s*/,'').replace(/\s*$/,'')
            if (self.content == ""){
                return;
            }
            $.post(uri, params).done((data) => {
                console.log(data);
                self.successAction("Комментарий отправлен!")
                self.getComments()
                self.content = ""
            }).fail((error) => {
                console.log(error)
            })
        },
        getComments(){
            let self = this,
                uri = '/api/1/comment/' + self.type + '/' + self.unique + '/' + this.getSess() + '/';

            $.get(uri, params).done((data) => {
                console.log(data);
                self.comments = data.response
            }).fail((error) => {
                console.log(error)
            })
        },
        getSess(){
            return document.getElementById('session_id').innerHTML;
        },
        successAction(message){
            Materialize.toast(message, 4000);
        },
        setName(name){
            this.getter = name
            this.content = name + ", " + this.content
            document.querySelectorAll(".__comment label")[0].className = " active"
            document.querySelectorAll(".__comment input")[0].focus()
        }
    }

})

export default Comment