<template>
  <div class="home">
    <div class="home-controls">

    </div>
    <div v-if="store.loading > 0">Loading</div>
    <div v-else>
      <div v-for="(memo, index) in store.memos" :key="memo" class="audio-list">
        <div v-if="!isActive(index)">
          {{ memo.filename }}
          <AudioPlayer  autoplay :filename="memo.filename" @click="console.log(index)" />
        </div>
        <div v-else>
          {{ memo.filename }}
          <AudioPlayer autoplay :filename="memo.filename" @click="console.log(index)" />
          <audio controls style="width: 100%">
          <source type="">
          Your browser does not support the audio element.
        </audio>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from '@/data/store'
import AudioPlayer from '@/components/AudioPlayer.vue'

export default {
  name: 'HomeView',
  components: {
    AudioPlayer,
  },
  methods: {
    isActive(memoIndex) {
      if (memoIndex === this.store.activeMemo) {
        return true
      }
    }
  },
  computed: {
    store() {
      return useStore()
    }
  },
  beforeMount() {
    this.store.getMemos()
  }
}
</script>

<style scoped></style>
