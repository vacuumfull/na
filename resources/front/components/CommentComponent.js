import Vue from 'vue';
import $ from 'jquery';
import template from '../../tmp/components/comments.html';
import Materialize from 'materialize-css';

const Comment = Vue.extend({
    template,
    props: [ 'isLogin',  'type'],
    data(){
        return {
            content: "huihui",
            getter: "",
            comments: [],
        }
    },
    created(){
        $.ajaxSetup({
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            }
        })
        this.getComments()
    },
    methods: {
        create(){
            let self = this,
                uri = '/messages/' + self.type,
                id = document.getElementById("hidden-id").innerText,
                params = {
                    [self.type + 'Id']: id,
                    getter:  self.getter,
                    content:  self.content
                }
            self.getter = document.getElementById("getter-name").innerText
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
                id = document.getElementById("hidden-id").innerText,
                params = {
                    [self.type + 'Id'] : id
                };
            $.get(uri, params).done((data) => {
                self.comments = data.response
            }).fail((error) => {
                console.log(error)
            })
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