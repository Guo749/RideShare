<template>
  <div class="main">
    <div class="body">
      <div class="login">
        <div>
          <el-input
            style="width: 300px"
            placeholder="username"
            type="tel"
            v-model="user.username"
          ></el-input>
        </div>
        <div>
          <el-input
            style="width: 300px"
            placeholder="password"
            v-model="user.password"
            show-password
          ></el-input>
        </div>

        <div></div>
        <el-button style="width: 300px" type="primary" v-on:click="login"
          >Login</el-button
        >
        <el-link target="_blank" type="primary">
          <router-link to="/createuser"
            >Do not have account? Create now!</router-link
          ></el-link
        >
        <div></div>
      </div>
    </div>
  </div>
</template>

<script>
import { loginUser, loadCar} from "../api/api.js";
export default {
  name: "login",
  data() {
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    login() {
      loginUser(this.user.username, this.user.password).then((response) => {
        console.log(response.data)
        this.$store.state.user.id = response.data.id
        this.$store.state.user.username = this.user.username
        this.$store.state.user.email    = response.data.email
        this.$store.state.login = true

        loadCar().then(response => {
          if(response.data.length != 0) {
            this.$store.commit('setCar', response.data[0])
            this.$store.state.user.hasCar = true 
          } else {
            console.log(this.car)
            this.$store.state.user.hasCar = false
          }
          this.$router.push('/startride')
        }, err => {
            alert(JSON.stringify(err.response.data))
        })
        console.log(this.$store.state.user)
      }, error => {
        alert("Check the username and password")
        console(error.response)
      });
    },
  },
  mounted: function() {
   console.log("in login.vue")
   console.log(this.$store.state.login)
   //console.log(this.$store.state.login)
   if(this.$store.state.login){
     this.$router.push('/startride')
   }
  },
};
</script>

<style>
.main {
  width: 100%;
  height: 654px;
  display: flex;
  flex-wrap: wrap;
  margin-top: -50px;
}
.header {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 70px;
  background-color: rgb(235, 245, 237);
  align-content: center;
}
.header > h3 {
  width: 50%;
}
.body {
  display: flex;
  flex-wrap: wrap;
  width: 100%;
  height: 584px;
  align-content: center;
  justify-content: center;
}
.login {
  width: 500px;
  height: 350px;
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  justify-content: center;
  border: 1px solid rgb(216, 225, 232);
  border-radius: 20px;
}
.login > div {
  width: 60%;
  height: 40px;
  margin-top: 10px;
  font-size: 30px;
}

.login > div:first-child {
  width: 60%;
  height: 40px;
  margin-top: -20px;
  font-size: 30px;
}
</style>
