import Vue from 'vue';
import $ from 'jquery';
import Materialize from 'materialize-css'
import template from '../../tmp/components/rating.html';

const Rate = Vue.extend({
    template,
    props: ['isLogin', 'type'],
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
            activated: false,
            showCommonRate: false
        }
    },
    created(){
        $.ajaxSetup({
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            }
        })
        this.getRate()
    },
    methods: {
        getRate(){
            let self = this,
                uri = '/rating/' + self.type,
                id = document.getElementById("hidden-id").innerText,
                params = {
                    [self.type + 'Id'] : id
                };
            $.get(uri, params).done(data => {
                self.allRate = data.response
                self.colorStars(self.allRate)
            })
        },
        colorStars(mark){
            console.log(mark)
            this.rate.forEach((item, i) => {
                if (mark > i) {
                    item.name = "star"
                } else {
                    item.name = "start_border"
                }
            })
        },
        unsetStars(){
            if (this.activated = false) {
                this.rate.forEach((item) => {
                    item.name = "start_border"
                })
            }
        },
        setStars(mark){
            let self = this,
                uri = "/rating/user/" + self.type,
                id = document.getElementById("hidden-id").innerText,
                params = {
                    rate: mark,
                    [self.type + 'Id']: id
                }
            self.activated = true
            self.colorStars(mark)
            $.post(uri, params).done(data => {
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
