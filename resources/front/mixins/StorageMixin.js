export default {
    data(){
        return {
            storage: localStorage
        }
    },
    methods: {
        storageSave(key, info){
            try {
                this.storage.setItem(key, info);
            } catch (e) {
                if (e == QUOTA_EXCEEDED_ERR) {
                    console.error('Quota exceeded!');
                }
            }
        },
        storageGet(key){
            let item = this.storage.getItem(key);
            console.log(item)
            return item;
        },
        storageRemove(key){
            this.storage.removeItem(key);
        },
        storageKey(n){
            return this.storage.key(n);
        },
        storageClear(){
            this.storage.clear();
        }
    }
}