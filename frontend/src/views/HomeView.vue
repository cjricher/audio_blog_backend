<template>
  <div class="home">
    <div class="home-controls"></div>
    <div v-if="store.loading > 0">Loading</div>
    <div v-else>

      <div class="accordion" id="audioAccordion">
        <div v-for="(memo, index) in store.memos" :key="memo" class="accordion-item">
          <h2 class="accordion-header">
            <button @click="setActive(memo)" class="accordion-button collapsed" :class="{active: isActive(memo)}" type="button" data-bs-toggle="collapse"
              :data-bs-target="'#collapse'+index">
              <div class="d-flex justify-content-between flex-wrap" style="width: 100%">
                <div>{{ memo.filename }}</div>
                <div style="padding-inline: 20px">[{{ prettyDate(memo.modified) }}]</div>
              </div>
            </button>
          </h2>
          <div v-show="isActive(memo)" :id="'collapse'+index" class="accordion-collapse collapse" data-bs-parent="#audioAccordion">
            <div class="accordion-body">
              <AudioPlayer :memo="memo"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from '@/data/store'
import AudioPlayer from '@/components/AudioPlayer.vue'
import { DateTime } from 'luxon';

export default {
  name: 'HomeView',
  components: {
    AudioPlayer,
  },
  methods: {
    prettyDate(datestring) {
      return DateTime.fromISO(datestring).toFormat('DD t')
    },
    isActive(memo) {
      if (this.store.activeMemo) {
        if (memo === this.store.activeMemo) {
          return memo.filename
        }
      }
    },
    setActive(memo) {
      this.store.stopAllAudio()
      console.log("SET")
      this.store.activeMemo = memo;
    }
  },
  computed: {
    store() {
      return useStore()
    }
  },
  beforeMount() {
    this.store.getMemos()
  },
}
</script>

<style scoped></style>
