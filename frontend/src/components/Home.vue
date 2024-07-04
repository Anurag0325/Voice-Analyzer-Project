<template>
  <div class="home-container">
    <h1>Welcome to the Home Page</h1>
    <button class="btn">
      <router-link to="/register" class="router-link">Register</router-link>
    </button>
    <button class="btn">
      <router-link to="/login" class="router-link">Login</router-link>
    </button>
  </div>
</template>
  
<script>
  export default {
    name: 'Home'
  };
</script>
  
<style scoped>
  .home-container {
    text-align: center;
    margin-top: 50px;
  }
  
  .btn {
    background-color: #4CAF50;
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border-radius: 8px;
  }
  
  .btn:hover {
    background-color: #45a049;
  }
</style>