<template>
  <div class="register-container">
    <h1>Register</h1>
    <form @submit.prevent="register" class="register-form">
      <label class="form-label">Username</label>
      <input type="text" v-model="username" class="form-input" required><br>
      <label class="form-label">Password</label>
      <input type="password" v-model="password" class="form-input" required><br>
      <label class="form-label">Email</label>
      <input type="email" v-model="email" class="form-input" required><br>
      <button type="submit" class="register-btn">Register</button>
    </form>
    <button @click="goToLoginPage" class="back-btn">Back to Login</button>
  </div>
</template>
  
<script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        email: ''
      };
    },

    methods: {
      async register() {
        try {
          const response = await fetch('http://localhost:5000/register', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              username: this.username,
              password: this.password,
              email: this.email,
            })
          });
          if (response.ok) {
            const data = await response.json();
            console.log('Registration successful:', data);
          } else {
            const errorData = await response.json();
            console.error('Registration failed:', errorData);
          }
        } catch (error) {
          console.error('Error registering user:', error);
        }
      },

      goToLoginPage() {
        this.$router.push('/');
      }
    }
  };
</script>
  
<style scoped>
  .register-container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .register-form {
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
    margin-bottom: 10px;
  }
  
  .form-input:focus {
    outline: none;
    border-color: #4CAF50;
  }
  
  .register-btn {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 12px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    cursor: pointer;
    border-radius: 4px;
    transition: background-color 0.3s ease;
    margin-bottom: 10px;
  }
  
  .register-btn:hover {
    background-color: #45a049;
  }
  
  .back-btn {
  background-color: #f44336;
  color: white;
  border: none;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s ease;
  margin-top: 10px;
}

.back-btn:hover {
  background-color: #d32f2f;
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