import Vue from 'vue';
import $ from 'jquery';
import GoogleMapsLoader from 'google-maps';
import Dialog from './components/DialogComponent';
import LeftMessages from './components/LeftMessagesComponent';
import LeftModal from './components/LeftModalComponent';
import UserMenu from './components/UserMenuComponent';

new Vue({
    el: '#index',
    components: {
        'dialog-component': Dialog,
        'left-messages': LeftMessages,
        'left-modal': LeftModal,
        'user-menu': UserMenu
    },
    data: {
        map: null,
        places: [],
        userInfo: {
            name: ""
        },
        messagesUnreadCount: 0,
    },
    created(){
        GoogleMapsLoader.KEY = 'AIzaSyAafNNNfqmsn7VHcU0rg1uw8BO0daZrj6Q'
        GoogleMapsLoader.load((google) => {
            new google.maps.Map(document.getElementById('map'), {
                center: { lat: 59.93961241484262, lng: 30.321905688476562},
                zoom: 12
            })
        })
    },
    mounted(){
        $('#left_message_window').modal();
        $(".button-collapse").sideNav();
        this.getPlaces()
    },
    watch: {
        places(val, newVal){
            if(val.length > 0){
                this.setLocations()
            }
        }
    },
    methods: {
        getPlaces(){
            let self = this,
                uri = "/api/1/map/";
            $.get(uri)
                .done(function(data) {
                    self.places = data;
                    self.setMap();
                })
                .fail(function(error) {
                    console.log(error);
                });
        },
        setMap(){
            GoogleMapsLoader.load((google) => {
                let map = new google.maps.Map(document.getElementById('map'), {
                    center: { lat: 59.93961241484262, lng: 30.321905688476562},
                    zoom: 12
                })
                this.map = map;
               
            })
        },
        openModal(userInfo){
            this.userInfo = userInfo;
        },
        openDialog(){
            $('#dialog_window').modal('open');
        },
        transportMessagesCount(messagesCount){
            this.messagesUnreadCount = messagesCount;
        },
        setLocations(){
            GoogleMapsLoader.load((google) => {
                let self = this,
                infowindow = new google.maps.InfoWindow();
                
                self.places.forEach((item) => {

                    let activeEvents = "",
                        marker,
                        coords = item.coordinates.split(","),
                        position = {
                            lat: parseFloat(coords[0]),
                            lng: parseFloat(coords[1]),
                        };

                    marker = new google.maps.Marker({
                        position:  position,
                        map: self.map,
                        title: item.title,
                        draggable: false,
                    });
                   
                    if (item.active_events !== undefined){
                        activeEvents += '<h6>Текущие события</h6><br>'
                        item.active_events.forEach(function(event){
                            activeEvents += `<a href="/events/${event.slug}">${event.title}</a><br>`
                        });
                    }

                    google.maps.event.addListener(marker, 'click', function() {
                        infowindow.setContent('<div>'+
                            '<h6><a href="/places/'+ item.slug +'">' + item.title + '</a></h6>' + '<br>' +
                            '<strong>' + item.description + '</strong><br>' +
                            '<br>' + activeEvents + '</div>');
                        infowindow.open(self.map, this);
                    });

                });
            })
           
        }
    }
})