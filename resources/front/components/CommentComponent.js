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
            getter: "",
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
                    [self.type + 'Id']: id,
                    getter: self.getter,
                    content: self.content
                },
                uri = '/api/1/rating/' + self.type + '/' + self.unique + '/' + this.getSess() + '/';
            self.getter = document.getElementById("getter-name").innerText;
            self.content = self.content.replace(/^\s*/,'').replace(/\s*$/,'')
            if (self.content == ""){
                return;
            }
            $.post(uri, params).done((data) => {
                self.successAction("Комментарий отправлен!")
                self.getComments()
                self.content = ""
            }).fail((error) => {
                console.log(error)
            })
        },
        getComments(){
            let self = this,
                uri = "/messages/"+ self.type +"/get",
                id = self.unique,
                params = {
                    [self.type + 'Id'] : id
                };
            $.get(uri, params).done((data) => {
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