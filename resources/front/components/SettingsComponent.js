import Vue from 'vue';
import Helper from '../mixins/HelperMixin';
import template from '../../tmp/components/settings.html';

const Settings = Vue.extend({
	template,
	mixins:[Helper],
	data(){
		return {
			settings: [],
			extend: [],
			preferMusic: [],
			styles: [
				{ tag:'house', image:'', id: 1 },
				{ tag:'trance', image:'', id: 2 },
				{ tag:'techno', image:'', id: 3 },
				{ tag:'chillout', image:'', id: 4 },
				{ tag:'acid techno', image:'', id: 5 },
				{ tag:'psy forest', image:'', id: 6 },
				{ tag:'ambient', image:'', id: 7 },
				{ tag:'noize', image:'', id: 8 },
				{ tag:'hard techno', image:'', id: 9 },
				{ tag:'electronic', image:'', id: 10 },
				{ tag:'psy chill', image:'', id: 11 },
				{ tag:'downtempo', image:'', id: 12 },
				{ tag:'trip hop', image:'', id: 13 },
				{ tag:'dub', image:'', id: 14 },
				{ tag:'raggie', image:'', id: 15 },
				{ tag:'trap', image:'', id: 16 },
				{ tag:'rap', image:'', id: 17 },
				{ tag:'rock', image:'', id: 18 },
			]
		}
	},
	watch:{
		preferMusic(val){
			if (val === null){
				setTimeout(() => {
					this.modalMusicOpen()
					this.preferMusic = []
				}, 3000)
			}
		}
	},
	mounted(){
		this.getSettings()
	},
	created(){
		 $('.chips').on('chip.add', function(e, chip){
			 console.log(chip)
		  });
		
		  $('.chips').on('chip.delete', function(e, chip){
			console.log(chip)
		  });
		
		  $('.chips').on('chip.select', function(e, chip){
			console.log(chip)
		  });
	},
	methods: {
		getSettings(){
			let self = this,
				uri = `/api/1/settings/current/${self.getSess()}`;
			fetch(uri, {method: "GET"})
				.then(response => response.json())
				.then(items => {
					self.settings = items.settings
					self.extend = items.extend
					self.preferMusic = items.extend[0].prefer_styles
				})
				.catch(error => console.error(error))
		},
		selectMusicStyle(event){
			let selected = event.target.innerHTML;
			this.preferMusic.unshift(selected)
			event.target.className += ' teal lighten-2';
			console.log(this.preferMusic)
		},
		addPreferMusic(){
			let self = this,
				uri = `/api/1/settings/music/`,
				data = new FormData();
			fetch(uri, {
					method: "POST", 
					body: `sessionid=${self.getSess()}&styles=${JSON.stringify(self.preferMusic)}`,
					headers: {
						"Content-type": "application/x-www-form-urlencoded; charset=UTF-8" 
					},
				})
				.then(response => response.json())
				.then(data => {
					console.log(data)
				})
				.catch(error => console.error(error))
		},
	}
})

export default Settings;