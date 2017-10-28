import Vue from 'vue';
import $ from 'jquery';
import template from '../../tmp/components/left-messages.html';

const LeftMessages = Vue.extend({
    template,
    props: ['user-role'],
    data(){
        return {
            showField: false,
            getter: '',
            users: [{ name: "Ivan" }]
        }
    },
    methods: {
        openField(){
            this.showField = true;
        },
        search(event){
            let uri = "/api/1/user/search",
                self = this,
                keyword = event.target.value;

            if (keyword.length > 2){
                self.users = [];
                $.get(uri, {
                    keyword: keyword
                })
                .done(function(data){
                    self.users =  data.response;
                })
                .fail(function(error) {
                    console.log(error);
                });
            }
        },
        selectGetter(event){
            let userInfo = {};
                userInfo['name'] = event.target.innerText;

            this.$emit('open-modal', userInfo);
            this.showField = false;
        }
    }

})

export default LeftMessages;
