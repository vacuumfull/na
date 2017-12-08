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
	}
}