import Vue from 'vue';
import $ from 'jquery';
import Materialize from 'materialize-css';
import template from '../../tmp/components/search.html';

const Search = Vue.extend({
    template,
    data() {
        return {
            tagFont: 12,
            showField: false,
            isFilled: false,
            showSearchResult: false,
            showPosts: false,
            showEvents: false,
            showPlaces: false,
            keyword: "",
            tags: [],
            posts: [],
            events: [],
            places: [],
        }
    },
    methods: {
        setKeyword(key){
            let self = this
            self.keyword = key
            self.isFilled = true
            self.search(self.keyword);
        },
        successAction(message){
            Materialize.toast(message, 4000);
        },
        link(string){
            window.location = window.location.origin + string;
        },
        search(key){
            let self = this,
                uri = `/api/1/search/default/${key}`;

            $.get(uri)
                .done((data) => {
                    self.posts = data.response.posts;
                    self.events = data.response.events;
                    self.places = data.response.places;
                    if (self.places.length > 0){
                        self.showPlaces = true;
                    } else {
                        self.showPlaces = false;
                    }
                    if (self.posts.length > 0){
                        self.showPosts = true;
                    } else {
                        self.showPosts = false;
                    }
                    if (self.events.length > 0){
                        self.showEvents = true;
                    } else {
                        self.showEvents = false;
                    }
                    if (self.events.length > 0 || self.places.length > 0 || self.posts.length > 0){
                        self.successAction("Что-то нашлось!");
                        let main = document.getElementById("main_page");
                        if (main != null){
                            main.remove();
                        }
                    } else {
                        self.successAction("Ничего нет по запросу!");
                    }

                }).fail(function(error){
                    console.log(error)
                })
        },
        getTags(){
            let self = this,
                uri = "/api/1/search/tags";
            $.get(uri)
                .done((data) => {
                    self.tags = data
                }).fail((error) => {
                    console.log(error)
                });
        }
    }
})

export default Search;
