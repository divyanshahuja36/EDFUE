<template>
  <div class="landing-page">
    <!-- Extended Blue Header/Nav -->
    <el-header class="header-bar">
      <div class="container nav-content">
        <h1 class="brand-name">Careers<span class="ai">AI</span></h1>
      </div>
    </el-header>

    <!-- Hero Section -->
    <section class="hero-section container">
      <el-row :gutter="20" align="middle">
        <el-col :xs="24" :md="12">
          <h2>AI-Powered Career Counseling</h2>
          <h3>Get personalized career guidance based on your psychometric profile</h3>
          <p>
            Simply upload your psychometric test results and chat with our AI counselor 
            to uncover the best career paths for you.
          </p>
          <div class="hero-buttons">
            <el-button type="primary" size="large" @click="goTo('register')">Get Started</el-button>
            <el-button type="primary" plain size="large" @click="goTo('login')">Sign In</el-button>
          </div>
        </el-col>
        <el-col :xs="24" :md="12" class="hero-image-col">
          <el-image 
            src="https://images.unsplash.com/photo-1552664730-d307ca884978?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"
            fit="cover"
            alt="AI counselor illustration"
            class="landing-img"
          />
        </el-col>
      </el-row>
    </section>

    <!-- Features Section -->
    <section class="features-section container">
      <el-row :gutter="20" justify="center" align="stretch">
        <el-col :xs="24" :sm="8" :md="8" v-for="feature in features" :key="feature.title">
          <el-card class="feature-card" shadow="hover">
            <el-icon class="feature-icon" :size="40">
              <component :is="feature.icon" />
            </el-icon>
            <h3>{{ feature.title }}</h3>
            <p>{{ feature.text }}</p>
          </el-card>
        </el-col>
      </el-row>
    </section>

    <!-- Bottom CTA Section -->
    <section class="cta-section">
      <div class="container cta-content">
        <h2>Ready to discover your ideal career path?</h2>
        <p>Our AI counselor is here to guide you. Take the next step in your career journey now.</p>
        <el-button class="cta-button" size="large" @click="goTo('register')">Get Started Now</el-button>
      </div>
    </section>
  </div>
</template>

<script setup>
import { UploadFilled, ChatRound, Compass } from '@element-plus/icons-vue'
import { useRouter } from 'vue-router'

const router = useRouter()
function goTo(route) {
  router.push('/' + route)
}

const features = [
  {
    icon: UploadFilled,
    title: 'Upload Psychometric Tests',
    text: 'Upload your assessment results for in-depth AI analysis.'
  },
  {
    icon: ChatRound,
    title: 'AI Counseling Sessions',
    text: 'Chat with an AI counselor for personalized guidance and support.'
  },
  {
    icon: Compass,
    title: 'Personalized Career Roadmap',
    text: 'Receive a custom career roadmap tailored to your profile.'
  }
]
</script>

<style scoped>
.landing-page {
  font-family: 'Segoe UI', sans-serif;
  background-color: #f9fbff;
  color: #1a1a1a;
}

.header-bar {
  background-color: #409eff;
  color: white;
  /* Extended height for the blue ribbon */
  padding: 2.5rem 0 2rem 0;
  min-height: 90px;
  display: flex;
  align-items: flex-end;
  border-bottom-left-radius: 32px;
  border-bottom-right-radius: 32px;
  box-shadow: 0 8px 32px rgba(64, 158, 255, 0.07);
}

.brand-name {
  font-size: 2.2rem;
  font-weight: 700;
  margin: 0;
  letter-spacing: 1px;
}

.brand-name .ai {
  color: #fff;
  background-color: #1a73e8;
  padding: 0.2rem 0.7rem;
  border-radius: 6px;
  margin-left: 6px;
}

.hero-section {
  padding: 4rem 0 3rem;
}

.hero-section h2 {
  font-size: 2.4rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.hero-section h3 {
  font-size: 1.4rem;
  color: #555;
  margin-bottom: 1rem;
}

.hero-section p {
  font-size: 1rem;
  color: #666;
  margin-bottom: 2rem;
  max-width: 600px;
}

.hero-buttons .el-button + .el-button {
  margin-left: 1rem;
}

.hero-image-col {
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 320px;
}

.landing-img {
  width: 100%;
  max-width: 350px;
  border-radius: 16px;
  box-shadow: 0 8px 24px rgba(0,0,0,0.10);
  margin: 0 auto;
  display: block;
}

.features-section {
  padding: 3rem 0;
  background-color: #ffffff;
}

.features-section .el-row {
  justify-content: center;
  align-items: stretch;
}

.feature-card {
  text-align: center;
  padding: 2rem 1rem;
  min-height: 270px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}

.feature-icon {
  color: #409eff;
  margin-bottom: 1rem;
}

.cta-section {
  background-color: #1a73e8;
  color: #fff;
  text-align: center;
  padding: 4rem 1rem;
}

.cta-section h2 {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1rem;
}

.cta-section p {
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

.cta-button {
  background-color: #fff;
  color: #1a73e8;
  font-weight: bold;
  border-radius: 4px;
  padding: 0.75rem 2rem;
  border: none;
}

.cta-button:hover {
  background: #e3edfa;
}

@media (max-width: 991px) {
  .header-bar {
    padding: 1.5rem 0 1rem 0;
    min-height: 70px;
    border-bottom-left-radius: 18px;
    border-bottom-right-radius: 18px;
  }
  .brand-name {
    font-size: 1.5rem;
  }
  .hero-section {
    padding: 2rem 0 1.5rem;
  }
  .landing-img {
    max-width: 250px;
  }
}
</style>
