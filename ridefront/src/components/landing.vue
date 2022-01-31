<!--   -->
<template>
  <div class="hello">
    
    <h1> Hello World </h1>
    <form action="">
      UserName<input type="text" placeholder="username" v-model="account.username"><br>
      Password<input type="text" placeholder="password" v-model="account.password"><br>
    </form>
    <button type="submit" @click="accountSubmit()">submit</button>
  </div>
  
</template>



<script>
import { createAccount } from "../api/api.js";
export default {
  name: 'landing',
  data(){
    return{
      msg: 'hello world',
      account: {
        "username": "",
        "password": "",
      },
    }

  },
  methods:{
    accountSubmit(){
      createAccount(this.account.username, this.account.password).then(response =>{
        console.log(this.account.username)
        console.log(this.account.password)
        
        console.log(response)
      })
    },
  }
}
</script>