<template>
  <div
    :class="[
      'rounded-2xl text-white p-6 shadow-md flex flex-col justify-between h-full',
      cardColorClass
    ]"
  >
    <div>
      <h3 class="text-xl font-semibold mb-2">{{ title }}</h3>
      <p class="text-sm">{{ description }}</p>
    </div>
    <button
      class="mt-4 bg-white text-sm font-medium text-black px-4 py-2 rounded-xl hover:bg-gray-200 transition"
    >
      {{ button }}
    </button>
  </div>
</template>


<script setup>
import { computed } from 'vue'

const props = defineProps({
  title: String,
  description: String,
  button: String,
  color: {
    type: String,
    default: 'blue',
  },
})

const cardColorClass = computed(() => {
  switch (props.color) {
    case 'blue':
      return 'bg-gradient-to-r from-blue-500 to-blue-700'
    case 'green':
      return 'bg-gradient-to-r from-green-500 to-green-600'
    case 'orange':
      return 'bg-gradient-to-r from-orange-400 to-yellow-500'
    default:
      return 'bg-gray-500'
  }
})
</script>
