<template>
  <el-container>
    <el-aside width="200px"></el-aside>

    <el-main>
      <el-form ref="form" label-width="80px">
        <el-form-item label="Destination">
          <el-input
            placeholder="Expect Destination Address"
            v-model="ride.destAddr"
          ></el-input>
        </el-form-item>

        <el-form-item label="Time">
          <el-col :span="10">
            <el-date-picker
              type="date"
              placeholder="Choose Date"
              value-format="yyyy-MM-dd"
              v-model="ride.date"
              style="width: 100%"
            ></el-date-picker>
          </el-col>
          <el-col :span="2"> -</el-col>
          <el-col :span="11">
            <el-time-picker
              v-model="ride.time"
              value-format="HH:mm:ss"
              e="width: 100%"
            ></el-time-picker>
          </el-col>
        </el-form-item>

        <el-form-item label="Number">
          <el-select v-model="ride.numPeople" placeholder="Number of People">
            <el-option label="1" value="1"></el-option>
            <el-option label="2" value="2"></el-option>
            <el-option label="3" value="3"></el-option>
            <el-option label="4" value="4"></el-option>
            <el-option label="5" value="5"></el-option>
            <el-option label="6" value="6"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="Joinable">
          <el-switch v-model="ride.isJoinable"></el-switch>
        </el-form-item>

        <el-form-item label="Other Info">
          <el-input type="textarea" v-model="ride.otherInfo"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="createRide">Publish</el-button>
        </el-form-item>
      </el-form>
    </el-main>
    <el-aside width="200px"></el-aside>
  </el-container>
</template>

<script>
import {postride, editride, deleride} from '../api/api.js'
export default {
  data() {
    return {
      ride: {
        destAddr: "",
        date: "",
        time: "",
        numPeople: "",
        isJoinable: false,
        otherInfo: "",
      },
    };
  },

  methods:{
      createRide: function(){
          postride(this.ride.destAddr, 
          this.ride.date, 
          this.ride.time, 
          this.ride.numPeople, 
          this.ride.isJoinable, 
          this.ride.otherInfo,
          this.$store.state.user.id).then((response) => {
            alert("Publish Info successfully")
            console.log(response.data)
            this.$router.push('/availableorder')
          }, (err) => {
            alert(JSON.stringify(err.response.data))
          })
      },
      editRide: function(){
          editride(this.ride.destAddr, 
          this.ride.arrivalDate, 
          this.ride.arrivalTime, 
          this.ride.numPeople, 
          this.ride.isJoinable, 
          this.ride.otherInfo).then((response) => {
              alert("edit successfully!")
          })        
      },
      onDelete: function(){
          deleride().then((response) => {
              alert("delete successfully!")
          })
      }
  }
};
</script>