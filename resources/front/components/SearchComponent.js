import Vue from 'vue';
import $ from 'jquery';
import Materialize from 'materialize-css';
import Helper from '../mixins/HelperMixin';
import template from '../../tmp/components/search.html';

const Search = Vue.extend({
    template,
    mixins: [Helper],
    data() {
        return {
            tagFont: 12,
            showField: false,
            isFilled: false,
            showSearchResult: true,
            keyword: "",
            tags: [],
            blogs: [],
            events: [],
            places: [],
        }
    },
    mounted(){
        this.getTags()
    },
    methods: {
        setKeyword(key){
            let self = this
            self.keyword = key
            self.isFilled = true
            self.search(self.keyword);
        },
        search(key){
            let self = this,
                uri = `/api/1/search/default/${key}`;

            $.get(uri)
                .done((data) => {
                    self.blogs = data.blogs;
                    self.events = data.events;
                    self.places = data.places;
                    if (self.events.length > 0 || self.places.length > 0 || self.posts.length > 0){
                        self.info("Что-то нашлось!");
                    } else {
                        self.info("Ничего нет по запросу!");
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
                    console.log(data)
                    self.tags = data
                }).fail((error) => {
                    console.log(error)
                });
        }
    }
})

export default Search;
