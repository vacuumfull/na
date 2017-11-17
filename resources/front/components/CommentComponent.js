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
                    app: self.type,
                    key: self.unique,
                    content: self.content,
                    sessionid: self.getSess()
                },
                uri = `/api/1/send/`;
            self.content = self.content.replace(/^\s*/,'').replace(/\s*$/,'')
            if (self.content === ""){
                return;
            }
            $.post(uri, params).done((data) => {
                if (data.success){
                    self.successAction("Комментарий отправлен!")
                    self.getComments()
                }
                self.content = ""
            }).fail((error) => {
                console.log(error)
            })
        },
        getComments(){
            let self = this,
                uri = `/api/1/comment/${self.type}/${self.unique}/${self.getSess()}/${self.offset}`;
            $.get(uri).done((data) => {
                self.comments = data.comments
            }).fail((error) => {
                console.log(error)
            })
        },
        getSess(){
            return document.getElementById('session_id').innerHTML;
        },
        formatDate(dateString){
            let date = new Date(dateString);
            let month = date.getDate() < 10 ? '0' + date.getDate().toString() : date.getDate();
            return `${date.getHours()}:${date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()}  ${month}/${parseInt(date.getMonth()) + 1}/${date.getFullYear()}`;
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