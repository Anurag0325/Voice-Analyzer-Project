<template>
  <div class="top-3-phrases-container">
    <h2>Top 3 Unique Phrases</h2>
    <ul>
      <li v-for="(phrase, index) in top3Phrases" :key="index" class="phrase-item">
        {{ phrase [0] }} times
        <br>
        {{ phrase[1] }} times
        <br>
        {{ phrase[2] }} times
      </li>
    </ul>
  </div>
</template>
  
<script>
  export default {
    props: {
      top3Phrases: {
        type: Array,
        required: true,
      }
    }
  };
</script>
  
  <style scoped>
.top-3-phrases-container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  font-family: 'Arial', sans-serif;
}

.header {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
  font-weight: bold;
}

ul {
  list-style-type: none;
  padding: 0;
}

.phrase-item {
  margin-bottom: 10px;
  padding: 10px;
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 5px;
  transition: background-color 0.3s;
  font-size: 16px;
}

.phrase-item:hover {
  background-color: #f1f1f1;
}

.phrase-item:nth-child(even) {
  background-color: #f9f9f9;
}

.phrase-item:nth-child(odd) {
  background-color: #fefefe;
}
</style>