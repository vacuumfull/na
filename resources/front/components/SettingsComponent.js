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
				{ tag:'house', image:'', id: 1, selected: false },
				{ tag:'trance', image:'', id: 2, selected: false },
				{ tag:'techno', image:'', id: 3, selected: false},
				{ tag:'chillout', image:'', id: 4, selected: false },
				{ tag:'acid techno', image:'', id: 5, selected: false },
				{ tag:'psy forest', image:'', id: 6, selected: false },
				{ tag:'ambient', image:'', id: 7, selected: false },
				{ tag:'noize', image:'', id: 8, selected: false },
				{ tag:'hard techno', image:'', id: 9, selected: false },
				{ tag:'electronic', image:'', id: 10, selected: false },
				{ tag:'psy chill', image:'', id: 11, selected: false },
				{ tag:'downtempo', image:'', id: 12, selected: false },
				{ tag:'trip hop', image:'', id: 13, selected: false },
				{ tag:'dub', image:'', id: 14, selected: false },
				{ tag:'raggie', image:'', id: 15, selected: false },
				{ tag:'trap', image:'', id: 16, selected: false },
				{ tag:'rap', image:'', id: 17, selected: false },
				{ tag:'rock', image:'', id: 18, selected: false },
			]
		}
	},
	watch:{
		preferMusic(val){
			let self = this;
			if (val === null){
				setTimeout(() => {
					self.modalMusicOpen()
					self.preferMusic = []
					$('.chips').material_chip();
					$('.chips-placeholder').material_chip({
						placeholder: 'Печатать сюда ',
						secondaryPlaceholder: 'еще?',
					});
					$('.chips').on('chip.add', function(e, chip){
						chip.selected = true;
						console.log(chip)
						self.styles.push(chip)
					 });
				   
					 $('.chips').on('chip.delete', function(e, chip){
					   console.log(chip)
					 });
				   
					 $('.chips').on('chip.select', function(e, chip){
					   console.log(chip)
					 });
				}, 3000)

			}
		}
	},
	mounted(){
		this.getSettings()
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
		addPreferMusic(){
			let self = this,
				uri = `/api/1/settings/music/`,
				data = new FormData(),
				selectedStyles = self.styles.filter(i => i.selected).map(i => i.tag)

			fetch(uri, {
					method: "POST", 
					body: `sessionid=${self.getSess()}&styles=${JSON.stringify(selectedStyles)}`,
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