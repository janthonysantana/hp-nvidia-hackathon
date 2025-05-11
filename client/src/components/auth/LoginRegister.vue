<template>
  <div class="min-h-screen bg-gradient-to-b from-[#7D23FF] to-[#B945F3] flex items-center justify-center px-4">
    <div class="bg-white p-8 rounded-2xl shadow-lg w-full max-w-md">
      <div class="flex justify-between mb-6">
        <button
          class="w-1/2 py-2 font-semibold rounded-l-xl transition"
          :class="isLogin
            ? 'bg-purple-600 text-white'
            : 'bg-gray-100 text-gray-800'"
          @click="isLogin = true"
        >
          Login
        </button>

        <button
          class="w-1/2 py-2 font-semibold rounded-r-xl transition"
          :class="!isLogin
            ? 'bg-purple-600 text-white'
            : 'bg-gray-100 text-gray-800'"
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
        <div class="mt-6 flex justify-center">
          <a
            href="http://localhost:5000/auth/google"
            class="flex items-center gap-2 bg-white border border-gray-300 hover:bg-gray-100 text-gray-800 font-medium py-2 px-4 rounded-xl transition"
          >
            <img src="https://www.svgrepo.com/show/475656/google-color.svg" alt="Google" class="w-5 h-5" />
            Sign in with Google
          </a>
        </div>
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
  let url = isLogin.value ? '/api/user/login' : '/api/user/signup'

  let payload
  let options

  if (isLogin.value) {
    payload = {
      identifier: form.value.email,
      password: form.value.password
    }

    options = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    }
  } else {
    payload = new FormData()
    payload.append('email', form.value.email)
    payload.append('password', form.value.password)
    payload.append('username', form.value.email.split('@')[0])
    payload.append('name', 'Default Name')
    payload.append('age', '25')
    payload.append('gender', 'other')
    payload.append('preferredLanguage', 'en')
    // optional: profile_picture if using file upload

    options = {
      method: 'POST',
      body: payload
    }
  }

  fetch(url, options)
    .then(res => res.json())
    .then(data => {
      if (data.access_token) {
        localStorage.setItem('token', data.access_token)
        router.push('/Dashboard')
        // redirect to dashboard or emit success event
        console.log('Logged in:', data)
      } else {
        alert(data.error || data.msg || 'Something went wrong')
      }
    })
    .catch(err => console.error(err))
}

</script>
