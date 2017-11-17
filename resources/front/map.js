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
        places: [],
        userInfo: {
            name: ""
        },
        messagesUnread: {},
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
    },
    methods: {
        getPlaces(){
            let self = this,
                uri = "/map/api";
            $.get(uri)
                .done(function(data) {
                    self.places = data.response;
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
                this.setLocations(map);
            })
        },
        openModal(userInfo){
            this.userInfo = userInfo;
        },
        openDialog(){
            $('#dialog_window').modal('open');
        },
        transportUserMessages(messagesUnread){
            this.messagesUnread = messagesUnread;
        },
        setLocations(map){
            let self = this,
                infowindow = new google.maps.InfoWindow();
            self.places.forEach(function(item){
                let activeEvents = "",
                    marker,
                    coords = item.coordinates.split(","),
                    position = {
                    lat: parseFloat(coords[0]),
                    lng: parseFloat(coords[1]),
                };

                if (item.icon === null){
                    marker = new google.maps.Marker({
                        position:  position,
                        map: map,
                        title: item.title,
                        draggable: false,
                    });
                } else {
                    let shape = {
                        coords: [1, 1, 1, 34, 32, 33, 34, 1],
                        type: 'poly'
                    };
                    let image = {
                        url: item.icon,
                        size: new google.maps.Size(40, 44),
                        origin: new google.maps.Point(0, 0),
                        anchor: new google.maps.Point(0, 44)
                    };
                    marker = new google.maps.Marker({
                        position: position,
                        icon: image,
                        shape: shape,
                        map: map,
                        title: item.title,
                        draggable: true,
                    });
                }
                if (item.active_events !== undefined){
                    activeEvents += '<h6>Текущие события</h6><br>'
                    item.active_events.forEach(function(event){
                        activeEvents += '<a href="/events/'+ event.id +'">' + event.title + '</a><br>'
                    });
                }

                google.maps.event.addListener(marker, 'click', function() {
                    infowindow.setContent('<div>'+
                        '<h6><a href="/places/'+ item.id +'">' + item.title + '</a></h6>' + '<br>' +
                        '<strong>' + item.description + '</strong><br>' +
                        '<br>' + activeEvents + '</div>');
                    infowindow.open(map, this);
                });

            });
        }
    }
})