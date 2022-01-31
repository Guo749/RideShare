<template>
  <el-container>
    <el-aside width="300px"></el-aside>

    <el-main>
      <el-form ref="form" label-width="80px">
        <el-form-item label="Car Type">
          <el-input v-model="car.type"></el-input>
        </el-form-item>
        <el-form-item label="Plate Num">
          <el-input v-model="car.licensePlateNumber"></el-input>
        </el-form-item>
        <el-form-item label="Capacity">
          <el-col :span="11">
            <el-select v-model="car.capacity" placeholder="Number of People">
            <el-option label="1" value="1"></el-option>
            <el-option label="2" value="2"></el-option>
            <el-option label="3" value="3"></el-option>
            <el-option label="4" value="4"></el-option>
            <el-option label="5" value="5"></el-option>
            <el-option label="6" value="6"></el-option>
          </el-select>
          </el-col>
        </el-form-item>
        <el-form-item label="Other Info">
          <el-input type="textarea" v-model="car.otherInfo"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onRegister" v-if="!hascar">Register</el-button>
          <el-button @click="onEdit" v-if="hascar">Edit</el-button>
          <el-button type="danger" @click="onDelete" v-if="hascar">Delete</el-button>
        </el-form-item>
      </el-form>
    </el-main>
    
    <el-aside width="300px"></el-aside>
  </el-container>
</template>

<script>
import { registercar, editcar, delcar, loadCar} from "../api/api.js";
export default {
  data() {
    return {
      car: {
        id: '',
        type: '',
        licensePlateNumber: '',
        capacity: '',
        otherInfo: '',
        owner: '' 
      }
    };
  },
  methods: {
    onRegister() {
      registercar(
        this.car.type,
        this.car.licensePlateNumber,
        this.car.capacity,
        this.car.otherInfo
      ).then((response) => {
          this.$store.commit('setCar', response.data)
          this.car = {...this.$store.state.user.car}
          console.log(this.car) 
          alert("register successfully")
          this.$router.push('/personinfo')
      }, err=> {
        alert(JSON.stringify(err.response.data))
      });
    },
    onEdit() {
      editcar(
        this.car.type,
        this.car.licensePlateNumber,
        this.car.capacity,
        this.car.otherInfo,
        this.car.id
      ).then((response) => {
        alert("edit successful");
        this.$store.commit('setCar', response.data)
        this.$router.push('/personinfo')
      }, err=> {
        alert(JSON.stringify(err.response.data))
      });
      console.log("submit!");
    },
    onDelete() {
      console.log(this.car.id)
      delcar(this.car.id).then((response) => {
        alert("delete successful");
        this.$store.commit('resetCar')
        this.$router.push('/personinfo')
      }, (err) => {
        alert(JSON.stringify(err.response.data))
      });
    },
  },
  mounted() {
    loadCar().then(response => {
        if(response.data.length != 0) {
          this.$store.commit('setCar', response.data[0])
          this.$store.state.user.hasCar = true
          this.car = {...this.$store.state.user.car}
          console.log(this.car)
        } else {
          this.$store.state.user.hasCar = false
          console.log(this.car)
        }
      }, err => {
        alert(JSON.stringify(err.response.data))
      })

      console.log(this.$store.state.user.hasCar)
 }, 
 computed: {
   hascar: function() {
     return this.car.id == '' ? false:true;
   }
 }
};
</script>