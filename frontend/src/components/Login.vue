<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="login" class="login-form">
      <label class="form-label">Username:</label>
      <input type="text" v-model="username" class="form-input" required><br>
      <label class="form-label">Password:</label>
      <input type="password" v-model="password" class="form-input" required><br>
      <button type="submit" class="login-btn">Login</button>
    </form>
    <button @click="goToRegister" class="register-btn">Register</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch('http://localhost:5000/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username: this.username, password: this.password }),
          credentials: 'include'
        });
        if (response.ok) {
          alert('Login successful!');
          this.$router.push('/dashboard');
        } else {
          const data = await response.json();
          alert('Login failed: ' + data.error);
        }
      } catch (error) {
        console.error('Error:', error);
      }
    },
    goToRegister() {
      this.$router.push('/register');
    }
  }
};
</script>
  
<style scoped>
.login-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.login-form {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  margin-bottom: 8px;
  color: #333;
  font-size: 16px;
}

.form-input {
  width: calc(100% - 22px);
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  transition: border-color 0.3s ease;
}

.form-input:focus {
  outline: none;
  border-color: #4CAF50;
}

.login-btn {
  background-color: #4CAF50;
  color: white;
  border: none;
  padding: 12px 20px;
  margin-top: 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.login-btn:hover {
  background-color: #45a049;
}

.register-btn {
  background-color: #2196F3;
  color: white;
  border: none;
  padding: 12px 20px;
  margin-top: 10px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
}

.register-btn:hover {
  background-color: #0b7dda;
}

.router-link {
  display: block;
  margin-top: 10px;
  text-decoration: none;
  color: blue;
}

.router-link:hover {
  text-decoration: underline;
}
</style>