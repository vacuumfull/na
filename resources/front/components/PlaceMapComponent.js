import Vue from 'vue';
import GoogleMapsLoader from 'google-maps';
import template from '../../tmp/components/place-map.html';

const PlaceMap = Vue.extend({
	template,
	props: ['coordinates', 'title'],
	data(){
		return {
			lat: null,
			lng: null
		}
	},
	mounted(){
        GoogleMapsLoader.KEY = 'AIzaSyAafNNNfqmsn7VHcU0rg1uw8BO0daZrj6Q';
	},
	created(){
		let coords = this.coordinates.split(',')
		this.lat = parseFloat(coords[0])
		this.lng = parseFloat(coords[1])
		setTimeout(() => {
			this.setCoordinates()
		}, 400)
	},
	methods: {
		setCoordinates(){
			let self = this;
			GoogleMapsLoader.load((google) => {
				let map = new google.maps.Map(document.getElementById('place-map'), {
					center: { lat: self.lat, lng: self.lng},
					zoom: 12
				})
				new google.maps.Marker({
					position: { lat: self.lat, lng: self.lng},
					map: map,
					title: self.title,
				});
			})
		}
	}
})

export default PlaceMap