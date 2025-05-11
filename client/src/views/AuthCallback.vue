<script setup>
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const token = route.query.token
const userId = route.query.userId

if (token && userId) {
  localStorage.setItem('token', token)
  localStorage.setItem('userId', userId)
  router.push('/')
} else {
  alert('Google sign-in failed.')
  router.push('/auth')
}
</script>
