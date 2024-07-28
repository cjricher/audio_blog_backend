<template>
  <div class="audio-card">
    <audio controls style="width: 100%">
      <source :src="'http://127.0.0.1:5000/memo/' + memo.filename" type="audio/mp4">
      Your browser does not support the audio element.
    </audio>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AudioPlayer',
  props: ['memo', 'active'],
  data() {
    return {}
  },
}
</script>

<style scoped></style>
