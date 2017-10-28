import Vue from 'vue';
import $ from 'jquery';
import Materialize from 'materialize-css';

const LeftMenu = Vue.extend({
    props: ['avatar', 'name', 'email', 'role'],
    data(){
        return {
            getter: {
                id: "",
                name: "",
            },
            message: "",
            users: [],
            showAvatar: false,
            getMessage: false,
            showUsersField: false,
            showScroll: false,
            field: ""
        }
    },
    mounted(){
        $('#left_message_window').modal();
        $(".button-collapse").sideNav();
    },
    created() {
        $.ajaxSetup({
            headers: {
                'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
            }
        });
        this.field = $('meta[name="csrf-token"]').attr('content')
    },
    methods: {
        openField(){
            this.showUsersField = true;
        },
        getUsers(){
            let uri = "/user/users",
                self = this;

            $.get(uri)
                .done(function(data){
                    self.users =  data.response;

                })
                .fail(function(error) {
                    console.log(error);
                });
        },
        selectGetter(event){
            let self = this,
                name = event.target.innerText,
                id = event.target.id,
                label = document.querySelectorAll(".user-search label")[0];

            self.getter.id = id;
            self.getter.name = name;
            self.users = [];
            label.className = " active";
            $('#left_message_window').modal('open');

        },
        sendMessage(){
            let self = this,
                author = document.getElementById("username").innerText,
                uri = "/messages/create";

            $.post(uri, {
                author: author,
                getter: self.getter.name,
                content: self.message,
            })
                .done(function(data){
                    self.successAction("Cообщение отправлено!");
                })
                .fail(function(error) {
                    console.log(error);
                });

        },
        successAction(message){
            Materialize.toast(message, 4000);
        },

        checkHeight(classname){
            var field = document.querySelectorAll(classname)[0];
            var height = field.offsetHeight;
            return height;
        },
        search(event){
            var uri = "/user/search",
                self = this,
                keyword = event.target.value,
                height = self.checkHeight(".__select_users");

            if (height >  298){
                self.showScroll = true;
            }

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


    }
})

export default LeftMenu;