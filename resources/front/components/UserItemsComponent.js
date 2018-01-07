import Vue from 'vue';
import Helper from '../mixins/HelperMixin';
import template from '../../tmp/components/user-items.html';

const UserItems = Vue.extend({
    template,
    props: ['type'],
    mixins: [Helper],
    data(){
        return {
            showTable:false,
            items: []
        }
    },
    mounted(){
        this.getItems()
    },
    methods: {
        getItems(){
            let self = this,
                ses = self.getSess(),
                url = `/api/1/item/list/${self.type}/${ses}`;
            if (ses === false) {
                window.location = window.location.origin + '/404'
            }
            fetch(url, {method: 'GET'})
                .then(response => {
                    return response.json()
                })
                .then(items => {
                    self.items = items;
                    if (self.items.length > 0) self.showTable = true;
                })
                .catch(error => {
                    console.error(error)
                })

        },
        removeItem(id, rowId){
            let self = this,
                uri = `/api/1/item/remove/`,
                data = new FormData();
                console.log(rowId)
            fetch(uri, {
                    method: "POST", 
                    body: `sessionid=${self.getSess()}&app=${self.type}&item_id=${id}`,
                    headers: {
                        "Content-type": "application/x-www-form-urlencoded; charset=UTF-8" 
                    },
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success){
                        document.getElementById(rowId).remove()
                    }
                })
                .catch(error => console.error(error))
            }
    }
})

export default UserItems;