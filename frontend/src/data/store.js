import { defineStore } from "pinia";
import axios from "axios";

export const useStore = defineStore('store', {
    state: () => ({  // Variables
        memos: [],
        activeMemo: 1,
        activeMemoName: null,
        loading: 0,
    }),
    actions: {  // Methods
        getMemos() {  // Pull some memos from assets
            this.loading += 1;
            try {
                axios.get('http://127.0.0.1:5000/memos').then((response) => {
                    this.memos = response.data
                })
            } catch (error) {
                console.error('Failed to fetch memos:', error)
            }
            this.loading -= 1;
        }
    },
})
