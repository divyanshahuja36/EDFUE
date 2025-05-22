<template>
    <div class="counselling-session-page">
      <h2>Counselling Session</h2>
      <!-- ElevenLabs Agent Widget -->
      <div id="elevenlabs-widget-container"></div>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue'
  
  onMounted(() => {
    // Only add the widget if it hasn't already been added
    if (!document.getElementById('elevenlabs-convai-widget')) {
      // Create the widget element
      const widget = document.createElement('elevenlabs-convai')
      widget.setAttribute('agent-id', 'agent_01jvrp4mj0ek9v3522fhtzw1ve')
      widget.id = 'elevenlabs-convai-widget'
  
      // Add widget to container
      document.getElementById('elevenlabs-widget-container').appendChild(widget)
  
      // Add the script tag if it doesn't exist
      if (!document.getElementById('elevenlabs-convai-script')) {
        const script = document.createElement('script')
        script.src = 'https://elevenlabs.io/convai-widget/index.js'
        script.async = true
        script.type = 'text/javascript'
        script.id = 'elevenlabs-convai-script'
        document.body.appendChild(script)
      }
    }
  })
  </script>
  
  <style scoped>
  .counselling-session-page {
    min-height: 60vh;
    padding: 2rem;
  }
  </style>
  