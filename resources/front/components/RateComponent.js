import Vue from 'vue';
import $ from 'jquery';
import Materialize from 'materialize-css'
import template from '../../tmp/components/rating.html';

const Rate = Vue.extend({
    template,
    props: ['isLogin', 'type', 'unique'],
    data(){
        return {
            rate: [
                { mark: 1, name: "star_border" },
                { mark: 2, name: "star_border" },
                { mark: 3, name: "star_border" },
                { mark: 4, name: "star_border" },
                { mark: 5, name: "star_border" },
                { mark: 6, name: "star_border" },
                { mark: 7, name: "star_border" },
                { mark: 8, name: "star_border" },
                { mark: 9, name: "star_border" },
                { mark: 10, name: "star_border" },
            ],
            allRate: 0,
            csrf: '',
            activated: false,
            showCommonRate: false
        }
    },
    created(){
        this.getRate()
        this.csrf =  this.getCookie('csrftoken');
        console.log(this.csrf);
        console.log(this.isLogin);
    },
    methods: {
        getRate(){
            let self = this,
                uri = '/api/1/rating/' + self.type + '/' + self.unique + '/' + self.csrf + '/';
               console.log(uri);
            $.get(uri).done(data => {
                console.log(data);
                if (data)
                self.allRate = data.response
                self.colorStars(self.allRate)
            })
        },
        colorStars(mark){
            this.rate.forEach((item, i) => {
                if (mark > i) {
                    item.name = "star"
                } else {
                    item.name = "star_border"
                }
            })
        },
        unsetStars(){
            if (this.activated = false) {
                this.rate.forEach((item) => {
                    item.name = "star_border"
                })
            }
        },
        getCookie(name){
            let cookies = document.cookie.split(';');
            for(let i=0 ; i < cookies.length ; ++i) {
                let pair = cookies[i].trim().split('=');
                if(pair[0] == name)
                    return pair[1];
            }
            return null;
        },  
        setStars(mark){
            let self = this,
                uri = '/api/1/vote/',
                params = {
                    sessionid: self.csrf,
                    app: self.type,
                    key: self.unique,
                    vote: mark
                };
                console.log(params);
            self.activated = true
            self.colorStars(mark)
            console.log(uri);
            $.post(uri, params).done(data => {
                console.log(data);
                self.getRate()
                self.successAction("Оценка учтена!")
            }).fail(error => {
                console.log(error)
            })
        },
        successAction(message){
            Materialize.toast(message, 4000)
        }
    }

})

export default Rate;
