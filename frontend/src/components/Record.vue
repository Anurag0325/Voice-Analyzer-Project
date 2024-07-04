<template>
  <div class="record-container">
    <h1 class="heading">Record and Translate</h1>
    <button @click="recordAndTranslate" class="record-btn">Record and Translate</button>
    <div v-if="recognizedText" class="result-container">
      <p class="result-text"><strong>Recognized:</strong> {{ recognizedText }}</p>
      <p class="result-text"><strong>Translated:</strong> {{ translatedText }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      recognizedText: null,
      translatedText: null,
    };
  },

  methods: {
    async recordAndTranslate() {
      try {
        const response = await fetch('http://localhost:5000/record', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          credentials: 'include'
        });
        if (response.ok) {
          const data = await response.json();
          this.recognizedText = data.recognized;
          this.translatedText = data.translated;
          this.$emit('dataUpdated');
        } else {
          console.error('Failed to fetch translation.');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
};
</script>

<style scoped>
.record-container {
  max-width: 600px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  background-color: #f9f9f9;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  text-align: center;
}

.heading {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.record-btn {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 12px 24px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  border-radius: 4px;
  margin-bottom: 20px;
}

.record-btn:hover {
  background-color: #45a049;
}

.result-container {
  margin-top: 20px;
  border: 1px solid #ccc;
  padding: 15px;
  background-color: #fff;
  border-radius: 8px;
  text-align: left;
}

.result-text {
  font-size: 18px;
  margin: 10px 0;
}
</style>