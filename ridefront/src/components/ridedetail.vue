<template>
  <el-container style="border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <el-row> </el-row>
      </el-header>

      <el-main style="height: 1000px">
        <el-dialog title="Edit Ride" :visible.sync="dialogFormVisible">
          <el-form ref="rideForm" label-width="80px">
            <el-form-item label="Destination">
              <el-input
                placeholder="Expect Destination Address"
                v-model="rideForm.destAddr"
              ></el-input>
            </el-form-item>

            <el-form-item label="Time">
              <el-col :span="10">
                <el-date-picker
                  type="date"
                  placeholder="Choose Date"
                  value-format="yyyy-MM-dd"
                  v-model="rideForm.date"
                  style="width: 100%"
                ></el-date-picker>
              </el-col>
              <el-col :span="2"> -</el-col>
              <el-col :span="11">
                <el-time-picker
                  v-model="rideForm.time"
                  value-format="HH:mm:ss"
                  e="width: 100%"
                ></el-time-picker>
              </el-col>
            </el-form-item>

            <el-form-item label="Number">
              <el-select
                v-model="rideForm.numPeople"
                placeholder="Number of People"
              >
                <el-option label="1" value="1"></el-option>
                <el-option label="2" value="2"></el-option>
                <el-option label="3" value="3"></el-option>
                <el-option label="4" value="4"></el-option>
                <el-option label="5" value="5"></el-option>
                <el-option label="6" value="6"></el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="Joinable">
              <el-switch v-model="rideForm.isJoinable"></el-switch>
            </el-form-item>

            <el-form-item label="Other Info">
              <el-input type="textarea" v-model="rideForm.otherInfo"></el-input>
            </el-form-item>

            <el-form-item>
              <el-button type="primary" @click="confirmEdit">Edit</el-button>
              <el-button type="primary" @click="cancel">Cancel</el-button>
            </el-form-item>
          </el-form>
        </el-dialog>

        <el-descriptions
          class="margin-top"
          title="Ride Detail"
          :column="3"
          :size="size"
          border
        >
          <template slot="extra">
            <el-button type="success" size="small" @click="hitEdit" v-if="myOwn"
              >Edit</el-button
            >
            <el-button type="primary" size="small" @click="hitJoin" v-if="hasRightToJoin"
              >Join</el-button
            >

            <el-button type="primary" size="small" @click="hitCancel" v-if="myShare" 
              >Cancel</el-button
            >

            <el-button type="primary" size="small" @click="hitClaim" v-if="hasRightToClaim"
              >Claim</el-button
            >

            <el-button type="primary" size="small" @click="hitComplete" v-if="hasRightToComplete"
              >Complete</el-button
            >

          </template>

          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-date"></i>
              Arrivate Date
            </template>
            {{ rideDetail.date }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-time"></i>
              Arrivate Time
            </template>
            {{ rideDetail.time }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-location-outline"></i>
              available seats
            </template>
            &nbsp {{ rideDetail.numPeople }} &nbsp
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-office-building"></i>
              Destination
            </template>
            {{ rideDetail.destAddr }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-setting"></i>
              Status
            </template>
            <el-tag size="small">{{ status }}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-check"></i>
              isJoinable
            </template>
            <el-switch
              v-model="rideDetail.isJoinable"
              disabled
              active-color="#13ce66"
              inactive-color="#ff4949"
            >
            </el-switch>
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-tickets"></i>
              Other Information
            </template>
            {{ rideDetail.otherInfo }}
          </el-descriptions-item>
        </el-descriptions>

        <el-descriptions
          class="margin-top"
          title="Driver Information"
          style="margin-top: 40px"
          v-if="hasDriver"
          :column="3"
          :size="size"
          border
        >
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-date"></i>
              DriverName
            </template>
            {{ driver.username }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-time"></i>
              Contact Info
            </template>
            {{ driver.email }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-location-outline"></i>
              Car Type
            </template>
            &nbsp {{ car.type }} &nbsp
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-office-building"></i>
              License Plate Number
            </template>
            {{ car.licensePlateNumber }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-tickets"></i>
              Capacity
            </template>
            {{ car.capacity }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-tickets"></i>
              Other Information
            </template>
            {{ car.otherInfo }}
          </el-descriptions-item>
        </el-descriptions>
      </el-main>
    </el-container>
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    </el-aside>
  </el-container>
</template>


<style>
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}

.noDecoration {
  text-decoration: none;
}
</style>

<script>
import { getDriverByFk, getCarByFk, editride, joinride, claimride, cancelRide, completeride, loadOpenRide} from "../api/api.js";
import _ from "lodash";

export default {
  data() {
    return {
      size: "",
      dialogFormVisible: false,
      driver: {
        username: "",
        email: "",
        id: "",
      },
      car: {
        id: "",
        type: "",
        licensePlateNumber: "",
        capacity: "",
        otherInfo: "",
        owner: "",
      },
      rideForm: {
        destAddr: "",
        date: "",
        time: "",
        numPeople: "",
        isJoinable: false,
        otherInfo: "",
      },
    };
  },
  methods: {
    init() {
      console.log("hasDriver: ", this.hasDriver)
      if (!!this.$store.state.user.currentRideDetail.driverID) {
        console.log(this.rideDetail.driverID)
        getDriverByFk(this.rideDetail.driverID).then(
          (response) => {
            console.log("this is driverInfo");
            console.log(response.data);
            this.driver = _.cloneDeep(response.data);
          },
          (err) => {
            alert(JSON.stringify(err.response.data));
          }
        );

        getCarByFk(this.rideDetail.driverID).then(
          (response) => {
            // this.car = _.cloneDeep(response.data)
            console.log("current info: ");
            console.log(response.data[0]);
            this.car = _.cloneDeep(response.data[0]);
          },
          (err) => {
            alert(JSON.stringify(err.response.data));
          }
        );
      }
    },
    hitCancel() {
      cancelRide(this.$store.state.user.currentRideDetail.id).then(
        (response) => {
          alert("cancel successfully")
          this.$router.push('/startride')
        }
      )
    },

    cancel() {
      this.$router.push("/personinfo");
    },
    confirmEdit() {
      console.log(this.$store.state.user.currentRideDetail.id)
      editride(this.rideForm.destAddr, 
          this.rideForm.date, 
          this.rideForm.time, 
          this.rideForm.numPeople, 
          this.rideForm.isJoinable, 
          this.rideForm.otherInfo, 
          this.$store.state.user.currentRideDetail.id).then((response) => {
              alert("edit successfully!")
              this.$router.push('/personinfo')
          })   
    },
    hitEdit(){
      this.dialogFormVisible = true
    },
    hitJoin(){
      joinride(this.$store.state.user.currentRideDetail.id, this.$store.state.user.id).then((response) => {
        alert("join successfully!")
        console.log(this.$store.state.user)
        this.$store.state.user.currentRideDetail.isJoinable = false;
        this.$store.state.user.currentRideDetail.shareID    = this.$store.state.user.id
        console.log(this.$store.state.user.currentRideDetail)
        this.$router.push('/availableorder')
        //this.$router.push('/joinride')
      })
    },
    hitClaim() {
      claimride(this.$store.state.user.currentRideDetail.id, this.$store.state.user.id).then((response) => {
        alert("claim successfully")
        this.$router.push('/availableorder')
      })
    },
    hitComplete(){
      completeride(this.$store.state.user.currentRideDetail.id).then((response) => {
        alert("complete it :) ")
        this.$router.push('/availableorder')
      })
    }
  },
  computed: {
    myOwn() {
      return this.$store.state.user.id == this.$store.state.user.currentRideDetail.rideOwner &&
             this.$store.state.user.currentRideDetail.status == 1;
    },
    myShare(){
      return this.$store.state.user.id == this.$store.state.user.currentRideDetail.shareID;
    },
    myDrive(){
      return this.$store.state.user.id == this.$store.state.user.currentRideDetail.driverID;
    },
    rideDetail() {
      return this.$store.state.user.currentRideDetail;
    },
    hasDriver() {
      return !!this.$store.state.user.currentRideDetail.driverID;
    },

    hasRightToJoin() {
      // 2. this ride is shareable
      // 3. this ride is not belonged to current user
      // 4. this ride's status is not completed
     // console.log(this.$store.state.user.currentRideDetail.rideOwner)
      //console.log(this.$store.state.user.id) 
      //console.log(this.$store.state.user.currentRideDetail.shareID)
      if (!this.$store.state.user.currentRideDetail.isJoinable) {
        return false;
      } else if (this.$store.state.user.currentRideDetail.rideOwner == this.$store.state.user.id) {
        return false;
      } else if (this.$store.state.user.currentRideDetail.state == 3) {
        return false;
      }else if(this.$store.state.user.currentRideDetail.shareID != null){
        return false;
      }
      return true;
    },
    hasRightToClaim() {
      console.log(!!this.$store.state.user.car.id)
      return !!this.$store.state.user.car.id  &&
       (this.$store.state.user.id != this.$store.state.user.currentRideDetail.rideOwner) &&
       (this.$store.state.user.id != this.$store.state.user.currentRideDetail.shareID) &&
        this.$store.state.user.currentRideDetail.status == 1;
    },
    hasRightToComplete() {
      return this.$store.state.user.id == this.$store.state.user.currentRideDetail.driverID &&
        this.$store.state.user.currentRideDetail.status == 2;
    },
    status() {
      return this.$store.state.user.currentRideDetail.status == 1 ? "start" :
             (this.$store.state.user.currentRideDetail.status == 2 ? "confirmed" : "completed")
    }
  },
  mounted() {
      loadOpenRide(this.$store.state.user.id).then(
      (response) => {
        if (response.data.length != 0) {
          this.tableData = _.cloneDeep(response.data);
        }
      },
      (err) => {
        alert("Something Went Wrong, May come back later")
      }
    ); 
    setTimeout(()=>{
        this.init()
      }, 500)
  },
};
</script>