import Vue from 'vue';
import GoogleMapsLoader from 'google-maps';
import template from '../../tmp/components/map.html';

const MapComponent = Vue.extend({
    template,
    props: ['showMap'],
    data(){
        return {
            map: {},
            marker: null,
            coordinates: "",
            position: {
                lat: 0,
                lng: 0,
            },
            icon: "",
            title: ""
        }
    },
    watch:{
        coordinates(val){ 
            this.$emit('set-coordinates', val);
        },
        showMap(val){
            let self = this;
            if (val){
                GoogleMapsLoader.load((google) => {

                    let map = new google.maps.Map(document.getElementById('map'), {
                        center: { lat: 59.93961241484262, lng: 30.321905688476562},
                        zoom: 12
                    })
            
                    google.maps.event.addListener(map, "rightclick", function(event) {
                    
                        if (self.marker !== null){
                            self.marker.setMap(null);
                        }

                        let lat = event.latLng.lat();
                        let lng = event.latLng.lng();
                        self.position = {
                            lat: lat,
                            lng: lng,
                        };
                        self.coordinates = lat + ", " + lng;
                        
                        self.marker = new google.maps.Marker({
                            position: self.position,
                            map: map,
                            title: self.title,
                            draggable: true,
                        });
                       
                    });
                
                })
            }
        }
    },
    mounted(){
        GoogleMapsLoader.KEY = 'AIzaSyAafNNNfqmsn7VHcU0rg1uw8BO0daZrj6Q';
    },
    setMarkerIcon(){
        let self = this;
        GoogleMapsLoader.load((google) => {
            let shape = {
                coords: [1, 1, 1, 34, 32, 33, 34, 1],
                type: 'poly'
            };
            let image = {
                url: self.icon,
                size: new google.maps.Size(40, 44),
                origin: new google.maps.Point(0, 0),
                anchor: new google.maps.Point(0, 44)
            };
            marker = new google.maps.Marker({
                position: self.position,
                icon: image,
                shape: shape,
                map: map,
                title: self.title,
                draggable: true,
            });
        })
    }
})
export default MapComponent;