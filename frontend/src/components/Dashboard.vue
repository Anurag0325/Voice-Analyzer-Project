<template>
  <div class="dashboard-container">
    <nav class="navbar">
      <h1 class="navbar-title">Dashboard</h1>
      <button @click="logout" class="logout-btn">Logout</button>
    </nav>
    <div class="content">
      <Record @dataUpdated="fetchData" />
      <WordFrequencies :wordFrequencies="wordFrequencies" :currentUser="currentUser" />
      <Top3Phrases :top3Phrases="top3Phrases" />
    </div>
  </div>
</template>
  
<script>
  import Record from './Record.vue';
  import WordFrequencies from './WordFrequencies.vue';
  import Top3Phrases from './Top3Phrases.vue';
  
  export default {
    components: {
      Record,
      WordFrequencies,
      Top3Phrases,
    },

    data() {
      return {
        currentUser: null,
        wordFrequencies: null,
        top3Phrases: [],
      };
    },

    methods: {
      async fetchData() {
        await this.fetchWordFrequencies();
        await this.fetchTop3Phrases();
      },

      async fetchWordFrequencies() {
        try {
          const response = await fetch('http://localhost:5000/word-frequencies', {
            method: 'GET',
            credentials: 'include'
          });
          if (response.ok) {
            this.wordFrequencies = await response.json();
          } else {
            console.error('Failed to fetch word frequencies:', await response.json());
          }
        } catch (error) {
          console.error('Error fetching word frequencies:', error);
        }
      },

      async fetchTop3Phrases() {
        try {
          const response = await fetch('http://localhost:5000/top-3-phrases', {
            method: 'GET',
            credentials: 'include'
          });
          if (response.ok) {
            this.top3Phrases = await response.json();
          } else {
            console.error('Failed to fetch top 3 phrases:', await response.json());
          }
        } catch (error) {
          console.error('Error fetching top 3 phrases:', error);
        }
      },

      async logout() {
        try {
          const response = await fetch('http://localhost:5000/logout', {
            method: 'GET',
            credentials: 'include'
          });
          if (response.ok) {
            window.location.href = '/';
          } else {
            console.error('Failed to logout:', await response.json());
          }
        } catch (error) {
          console.error('Error logging out:', error);
        }
      },
    },

    mounted() {
      this.fetchData();
      setInterval(this.fetchData, 5000);
    },
  };
</script>
  
<style scoped>
.dashboard-container {
  max-width: 800px;
  margin: auto;
  padding: 20px;
}

.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #333;
  color: white;
  padding: 10px 20px;
  margin-bottom: 20px;
}

.navbar-title {
  margin: 0;
}

.logout-btn {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
}

.logout-btn:hover {
  background-color: #d32f2f;
}

.content {
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
}
</style>