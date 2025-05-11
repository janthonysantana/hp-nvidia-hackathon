<template>
  <div class="bg-white p-6 rounded-xl shadow h-full">
    <h2 class="text-lg font-semibold mb-4 text-gray-700">Daily Missions</h2>
    <ul class="space-y-3">
      <li
        v-for="(task, index) in tasks"
        :key="index"
        class="flex items-center justify-between px-4 py-3 rounded-lg border"
        :class="task.completed ? 'bg-green-50 border-green-300' : 'bg-gray-50 border-gray-200'"
      >
        <div class="flex items-center gap-3">
          <input
            type="checkbox"
            v-model="task.completed"
            class="w-4 h-4 text-blue-600 rounded border-gray-300"
          />
          <span
            :class="task.completed ? 'line-through text-gray-400' : 'text-gray-800'"
            class="text-sm"
          >
            {{ task.text }}
          </span>
        </div>
        <span
          v-if="task.completed"
          class="text-green-600 text-xs font-semibold"
        >
          Done
        </span>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const tasks = reactive([
  { text: 'Log your morning glucose', completed: true },
  { text: 'Drink 8oz of water', completed: false },
  { text: 'Eat a balanced breakfast', completed: false },
  { text: 'Do a 10-min walk', completed: false },
])
</script>
