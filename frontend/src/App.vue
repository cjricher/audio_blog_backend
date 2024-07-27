<template>
  <NavBar/>
  <HomeView/>
</template>

<script>
import HomeView from './views/HomeView.vue'
import NavBar from './components/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    HomeView,
  },
}
</script>

<style scoped>
</style>
