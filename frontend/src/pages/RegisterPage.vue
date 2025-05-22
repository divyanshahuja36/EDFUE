<template>
    <div class="register-page">
      <el-card class="register-card">
        <h2 class="register-title">Create Your Account</h2>
        <el-form :model="form" :rules="rules" ref="registerForm" label-width="130px" @submit.prevent="onSubmit">
          <el-form-item label="Full Name" prop="full_name">
            <el-input v-model="form.full_name" autocomplete="name" />
          </el-form-item>
          <el-form-item label="Email" prop="email">
            <el-input v-model="form.email" autocomplete="email" />
          </el-form-item>
          <el-form-item label="Grade/Class" prop="grade_class">
            <el-input v-model="form.grade_class" placeholder="e.g., 12th Grade, College Freshman" />
          </el-form-item>
          <el-form-item label="Contact Number" prop="contact">
            <el-input v-model="form.contact" autocomplete="tel" />
          </el-form-item>
          <el-form-item label="Expectations" prop="expectations">
            <el-input
              type="textarea"
              v-model="form.expectations"
              placeholder="What are you hoping to achieve with our platform?"
            />
          </el-form-item>
          <el-form-item label="Password" prop="password">
            <el-input v-model="form.password" show-password autocomplete="new-password" />
          </el-form-item>
          <el-form-item label="Confirm Password" prop="confirmPassword">
            <el-input v-model="form.confirmPassword" show-password autocomplete="new-password" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" :loading="loading" @click="onSubmit">Sign Up</el-button>
            <span class="login-link">Already a user?
              <router-link to="/login" style="color: #409eff;">Login</router-link>
            </span>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </template>
  
  <script setup>
  import { ref, reactive } from 'vue'
  import { useRouter } from 'vue-router'
  import { ElMessage } from 'element-plus'
  
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
  
  const rules = {
    full_name: [
      { required: true, message: 'Full name is required', trigger: 'blur' },
      { min: 2, message: 'Name must be at least 2 characters', trigger: 'blur' }
    ],
    email: [
      { required: true, message: 'Email is required', trigger: 'blur' },
      { type: 'email', message: 'Invalid email address', trigger: 'blur' }
    ],
    grade_class: [
      { required: true, message: 'Grade/Class is required', trigger: 'blur' }
    ],
    contact: [
      { required: true, message: 'Contact number is required', trigger: 'blur' }
    ],
    password: [
      { required: true, message: 'Password is required', trigger: 'blur' },
      { min: 6, message: 'Password must be at least 6 characters', trigger: 'blur' }
    ],
    confirmPassword: [
      { required: true, message: 'Confirm password is required', trigger: 'blur' },
      {
        validator: (rule, value) => value === form.password,
        message: 'Passwords must match',
        trigger: 'blur'
      }
    ]
  }
  
  const onSubmit = () => {
    registerForm.value.validate(async (valid) => {
      if (!valid) return
      loading.value = true
      try {
        // Replace with your API call or registration logic
        // await registerUser({ ...form })
        ElMessage.success('Registration successful! You can now log in.')
        router.push('/login')
      } catch (err) {
        ElMessage.error('Registration failed. Please try again.')
      } finally {
        loading.value = false
      }
    })
  }
  </script>
  
  <style scoped>
  .register-page {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f9fbff;
  }
  .register-card {
    max-width: 420px;
    width: 100%;
    padding: 2rem 2.5rem;
    box-shadow: 0 4px 24px rgba(64, 158, 255, 0.08);
  }
  .register-title {
    text-align: center;
    margin-bottom: 1.5rem;
    font-weight: 600;
    color: #409eff;
  }
  .login-link {
    margin-left: 1.5rem;
    font-size: 0.95rem;
  }
  </style>
  