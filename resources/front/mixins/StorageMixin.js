export default {
    data(){
        return {
            storage: localStorage
        }
    },
    methods: {
        storageSave(key, info){
            console.log('hi');
            try {
                this.storage.setItem(key, info);
            } catch (e) {
                if (e == QUOTA_EXCEEDED_ERR) {
                    console.error('Quota exceeded!');
                }
            }
        },
        storageGet(key){
            return this.storage.getItem(key);
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