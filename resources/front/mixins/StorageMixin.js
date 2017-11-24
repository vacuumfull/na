export default {
    data(){
        return {
            storage: localStorage
        }
    },
    methods: {
        storageSave(key, info){
            try {
                this.storage.setItem(key, JSON.stringify(info));
            } catch (e) {
                if (e == QUOTA_EXCEEDED_ERR) {
                    console.error('Quota exceeded!');
                }
                return false;
            }
        },
        storageGet(key){
            return JSON.parse(this.storage.getItem(key));
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