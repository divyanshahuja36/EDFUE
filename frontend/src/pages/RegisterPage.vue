<template>
  <!-- Template remains the same -->
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import axios from 'axios'  // ⭐ Added axios import

const router = useRouter()
const loading = ref(false)
const registerForm = ref(null)

const form = reactive({
  full_name: '',
  email: '',
  grade_class: '',
  contact: '',
  expectations: '',
  password: '',
  confirmPassword: ''
})

const rules = { /* Keep existing rules */ }

const onSubmit = () => {
  registerForm.value.validate(async (valid) => {
    if (!valid) return
    loading.value = true
    try {
      // ⭐ Actual API call
      const { confirmPassword, ...registrationData } = form
      await axios.post('http://localhost:8000/api/register', registrationData)
      
      ElMessage.success('Registration successful! You can now log in.')
      router.push('/login')
    } catch (err) {
      // ⭐ Improved error handling
      const errorMessage = err.response?.data?.detail || 'Registration failed. Please try again.'
      ElMessage.error(errorMessage)
    } finally {
      loading.value = false
    }
  })
}
</script>

<style scoped>
/* Styles remain the same */
</style>
