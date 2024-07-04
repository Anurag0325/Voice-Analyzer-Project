<template>
  <div class="word-frequencies-container">
    <h1>Word Frequencies</h1>
    <div v-if="wordFrequencies" class="table-container">
      <h2>{{ currentUser }} Word Frequencies</h2>
      <table>
        <thead>
          <tr>
            <th>Word</th>
            <th>Frequency</th>
            <th>Overall Frequency</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(frequency, word) in wordFrequencies.user_word_freq" :key="word">
            <td>{{ word }}</td>
            <td>{{ frequency }}</td>
            <td>{{ wordFrequencies.all_word_freq[word] || 0 }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
  
<script>
  export default {
    props: {
      wordFrequencies: {
        type: Object,
        required: true,
      },
    },

    computed: {
        currentUser() {
            return this.wordFrequencies.currentUser;
        }
    }
  };
</script>
  
<style scoped>
.word-frequencies-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.table-container {
  margin-top: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 12px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
  color: #333;
}

td {
  background-color: #fff;
  color: #555;
}

tbody tr:nth-child(odd) {
  background-color: #f9f9f9;
}

tbody tr:hover {
  background-color: #f1f1f1;
}

h1, h2 {
  color: #333;
  text-align: center;
}
</style>