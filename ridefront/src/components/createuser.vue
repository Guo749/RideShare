<template>
  <div class="main">
    <div class="body">
      <div class="login">
        <div>
          <el-input
            style="width: 300px"
            placeholder="username"
            type="tel"
            v-model="user.username">
          </el-input>
        </div>        
        <div>
          <el-input
            style="width: 300px"
            placeholder="email"
            type="tel"
            v-model="user.email">
          </el-input>
        </div>

        <div>
          <el-input
            style="width: 300px"
            placeholder="password"
            v-model="user.password"
            show-password
          ></el-input>
          <el-input
            style="width: 300px"
            placeholder="password"
            v-model="password2"
            show-password
          ></el-input>
        </div>

        <div></div>
        <div class="btnbtn">
        <el-button style="width: 300px" type="primary" v-on:click="checkAndCreate">create</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {postUser} from '../api/api.js'
export default {
  name: "createuser",
  data() {
    return {
      user:{
        "username": "",
        "email": "",
        "password": "",
      },
      password2: "",
    };
  },
  methods:{
    checkAndCreate() {
      if(this.user.password === this.password2){
        //create user
        postUser(this.user.username, this.user.password, this.user.email).then((response) => {
          alert("please return to login page and login again")
          this.$store.state.tempUserName = this.user.username
          this.$store.state.tempPassword = this.user.password
          
          this.$router.push('/')
        }, (error) => {
          console.log(error.response.data)
          alert(JSON.stringify(error.response.data))
        })
      }else{
        alert("two passwords not equal!")
      }
    }
  }
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
