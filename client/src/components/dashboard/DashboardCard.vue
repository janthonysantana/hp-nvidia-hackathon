<template>
  <div class="bg-white shadow rounded-xl p-6">
    <h2 class="text-gray-500 text-sm uppercase">{{ title }}</h2>
    <p class="text-2xl font-bold mt-2 text-gray-500">{{ value }}</p>
  </div>
</template>

<script setup>
defineProps(['title', 'value'])
</script>
