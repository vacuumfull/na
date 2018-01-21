import Vue from 'vue';
import Helper from '../mixins/HelperMixin';
import $ from 'jquery';
import template from '../../tmp/components/tags.html';

const TagsComponent = Vue.extend({
	template,
	mixins: [Helper],
	data(){
		return {
			tags: []
		}
	},
	mounted(){
		this.init()
	},
	methods: {
		init(){
			let self = this,
				currLocation = window.location.href;
			$('.chips').material_chip();
			$('.chips-placeholder').material_chip({
				placeholder: 'Печатать сюда ',
				secondaryPlaceholder: 'еще?',
			});
			$('.chips').on('chip.add', function(e, chip){
				if (self.tags.length === 5){
					$('.chips').material_chip({
						data: self.tags
					});
					return self.info('Не более 5 тэгов!')
				}
				if (self.tags.length <= 5){
					self.tags = $('.chips').material_chip('data')
					self.setTags(self.tags)
				}
			});
			$('.chips').on('chip.delete', function(e, chip){
				self.tags = $('.chips').material_chip('data')
				if (self.tags.length === 0){
					return self.info('Нужен хотя бы 1 тэг!')
				}
			});
			if (currLocation.includes('/edit/')){
				self.getCurrentTags()
			}
		},
		setTags(tags){
			let str = '', input = document.getElementById('id_tags');
			tags.forEach(item => {
				str += item.tag + ','
			})
			input.value = str
		},
		getCurrentTags(){
			let tags = document.getElementById('id_tags').value;
			this.tags = tags.split(',').filter(x => x !== "").map(item => item = {tag: item})
			$('.chips').material_chip({
				data: this.tags
			});
		}
	}
})

export default TagsComponent