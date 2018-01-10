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
					if (!currLocation.includes('/edit/')){
						self.setTags(self.tags)
					} else {
						self.setTagToSelect(chip.tag)
					}
				}
			});
			$('.chips').on('chip.delete', function(e, chip){
				self.tags = $('.chips').material_chip('data')
				if (self.tags.length === 0){
					return self.info('Нужен хотя бы 1 тэг!')
				}
				if (currLocation.includes('/edit/')){
					self.removeTagFromSelect(chip.tag)
				}
			});
			if (currLocation.includes('/edit/')){
				self.getCurrentTags()
			}
		},
		setTags(tags){
			let str = '', input = document.getElementById('id_tags');
			tags.forEach(item => {
				str += item.tag + '|'
			})
			input.value = str
		},
		setTagToSelect(tag){
			let option = document.createElement('option'),
				select = document.getElementById('id_tags');
			option.innerText = tag;
			option.selected = 'selected';
			option.value = tag;
			select.appendChild(option)
		},
		removeAndReplace(){
			document.getElementById('id_tags').remove();

			let tagsInput = document.createElement('input'),
				hiddenField = document.querySelectorAll('.__tags-field.__hidden')[0];

			tagsInput.id = 'id_tags'
			tagsInput.name = 'tags'
	
			hiddenField.appendChild(tagsInput)
		},
		removeTagFromSelect(tag){
			let select = document.getElementById('id_tags');
			for (let i = 0; i < select.length; i++){
				if (select.options[i].innerText === tag ){
					select.remove(i)
				}
			}
		},
		getCurrentTags(){
			let selectField = document.getElementById('id_tags'),
				selectedTags = [];
			for (let i = 0; i < selectField.options.length; i++){
				if (selectField.options[i].selected){
					selectedTags.push({tag: selectField.options[i].innerText})
				}
			}
			this.tags = selectedTags;
			$('.chips').material_chip({
				data: this.tags
			});
		}
	}
})

export default TagsComponent