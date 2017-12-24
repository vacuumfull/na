import Materialize from 'materialize-css';
import $ from 'jquery';

export default {
	methods: {
		formatDate(string){
            let date = new Date(string),
                hour = date.getHours(),
                minutes = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes(),
                day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate(),
                month = date.getMonth() + 1,
                year = date.getFullYear();  
            return `${day}/${month}/${year} ${hour}:${minutes}`;
        },
        encodeImageFileAsURL(event) {
            let filesSelected = event.target.files;
            if (filesSelected.length > 0) {
                let fileToLoad = filesSelected[0];
                let fileReader = new FileReader();

                fileReader.onload = function(fileLoadedEvent) {
                    let srcData = fileLoadedEvent.target.result; // <--- data: base64
                    let newImage = document.createElement('img');
                    newImage.src = srcData;
                    newImage.className = "responsive-img";
                    document.getElementById("img-field").innerHTML = newImage.outerHTML;
                }
                fileReader.readAsDataURL(fileToLoad);
            }
        },
        info(message){
            Materialize.toast(message, 4000);
        },
        getSess(){
            try {
                let ses = document.getElementById('session_id').innerHTML
                return ses;
            } catch (e) {
                console.error(e.message)
                return false;
            }
        },
        modalMusicOpen(){
            $('#modal-music').modal('open');
        },
        modalMusicClose(){
            $('#modal-music').modal('close');
        }
	}
}