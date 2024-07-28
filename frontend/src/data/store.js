import { defineStore } from "pinia";
import axios from "axios";

export const useStore = defineStore('store', {
    state: () => ({  // Variables
        memos: [],
        activeMemo: null,
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
        },
        stopAllAudio(reset=false) {
            const audioElements = document.getElementsByTagName('audio');
            for (let i = 0; i < audioElements.length; i++) {
                audioElements[i].pause();
                if (reset) {
                    audioElements[i].currentTime = 0; // Optional: Reset to the beginning
                }
            }
        }
    },
})
