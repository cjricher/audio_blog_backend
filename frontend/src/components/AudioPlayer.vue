<template>
  <div class="audio-card">
    {{ filename }}
    <audio controls style="width: 100%">
      <source :src="getMemoURL(filename)" type="audio/mp4">
      Your browser does not support the audio element.
    </audio>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AudioPlayer',
  props: [
    'filename',
  ],
  data() {
    return {
    }
  },
  computed: {
    getMemoURL(file) {
      console.log('FileName', file)
      if (file) {
        console.log('BEGIN LOADING')
        axios.get(`http://127.0.0.1:5000/memo/${file}`).then((response) => {
          console.log(response)
          return response
        })
      }
      console.log('NO GOOD')
    },
  }
}
</script>

<style scoped></style>
