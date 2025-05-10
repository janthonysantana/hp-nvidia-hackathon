<template>
  <div class="min-h-screen bg-gradient-to-b from-[#7D23FF] to-[#B945F3] flex items-center justify-center px-4">
    <div class="bg-white p-8 rounded-2xl shadow-lg w-full max-w-md">
      <div class="flex justify-between mb-6">
        <button
          class="w-1/2 py-2 font-semibold rounded-l-xl"
          :class="isLogin ? 'bg-purple-600 text-white' : 'bg-gray-100'"
          @click="isLogin = true"
        >
          Login
        </button>
        <button
          class="w-1/2 py-2 font-semibold rounded-r-xl"
          :class="!isLogin ? 'bg-purple-600 text-white' : 'bg-gray-100'"
          @click="isLogin = false"
        >
          Register
        </button>
      </div>

      <form @submit.prevent="handleSubmit">
        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700">Email</label>
          <input
            type="email"
            v-model="form.email"
            class="w-full px-4 py-2 mt-1 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-purple-500"
            required
          />
        </div>

        <div class="mb-4">
          <label class="block text-sm font-medium text-gray-700">Password</label>
          <input
            type="password"
            v-model="form.password"
            class="w-full px-4 py-2 mt-1 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-purple-500"
            required
          />
        </div>

        <div v-if="!isLogin" class="mb-4">
          <label class="block text-sm font-medium text-gray-700">Confirm Password</label>
          <input
            type="password"
            v-model="form.confirmPassword"
            class="w-full px-4 py-2 mt-1 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-purple-500"
            required
          />
        </div>

        <button
          type="submit"
          class="w-full py-2 mt-4 text-white bg-purple-600 hover:bg-purple-700 rounded-xl font-semibold transition"
        >
          {{ isLogin ? 'Login' : 'Register' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const isLogin = ref(true)
const form = ref({
  email: '',
  password: '',
  confirmPassword: ''
})

const handleSubmit = () => {
  if (!isLogin.value && form.value.password !== form.value.confirmPassword) {
    alert('Passwords do not match!')
    return
  }

  const route = isLogin.value ? '/api/login' : '/api/register'

  fetch(route, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(form.value)
  })
    .then(res => res.json())
    .then(data => {
      // handle success (store token, redirect, etc.)
      console.log(data)
    })
    .catch(err => console.error(err))
}
</script>
