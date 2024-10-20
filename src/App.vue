<script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<script>
export default {
  data() {
    return {
      message: 'Loading...'
    };
  },
  async mounted() {
    try {
      const response = await fetch('http://localhost:3000/api/message');
      const data = await response.json();
      this.message = data.message;
    } catch (error) {
      console.error('Error fetching message:', error);
      this.message = 'Failed to load message';
    }
  }
};
</script>

<template>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  {{ message }}
  <HelloWorld msg="Vite + Vue" />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
