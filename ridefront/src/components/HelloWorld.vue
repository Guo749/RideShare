<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul>
      <li v-for="(car, index) in car" :key="index" style="display:block">
        {{index}}-{{car.ownername}}-{{car.test}}
      </li>
    </ul>
    <form action="">
      输入车辆拥有者名字:<input type="text" placeholder="owner name" v-model="inputCar.ownername"><br>
      输入车牌号:<input type="text" placeholder="plate number" v-model="inputCar.test"><br>
    </form>
    <button type="submit" @click="carSubmit()">submit</button>
  </div>
</template>

<script>
import {getCar, postCar} from '../api/api.js'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      // books list data
      car: [
        {ownername: 'test', test: '1234'},
      ],
      // book data in the form
      inputCar: {
        "ownername": "",
        "test": "",
      }
    }
  },
  methods: {
    // loadCar () {
    //   getCar().then(response => {
    //     this.car = response.data
    //   })
    // }, 
    carSubmit () {
      postCar(this.inputCar.ownername, this.inputCar.test).then(response => {
        console.log(response)
        this.loadCar()
      })
    }
  },
  created: function () {
    // this.loadCar()
    console.log("hello")
  }
}
</script>