<script setup>
import { reactive } from 'vue'
import HealthBar from './vue/HealthBar.vue'
import HealthBarProgress from './vue/HealthBarProgress.vue'
import IncrementMenu from './vue/IncrementMenu.vue'

const model = reactive({
  _id: 'm1',
  name: 'HP',
  value: 8,
  total: 10,
  color: '#4caf50',
  healthBarColorMid: '#ffc107',
  healthBarColorLow: '#f44336'
})
</script>

<template>
  <div id="main-layout">
    <HealthBar :model="model" />
    <HealthBarProgress :model="model" />
    <IncrementMenu />
  </div>
</template>

<style>
/* Global styles for your layout can go here */
#main-layout {
  padding: 20px;
  font-family: sans-serif;
}
</style>