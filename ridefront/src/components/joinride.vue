<template>
  <el-container style="border: 1px solid #eee; height: 100%">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <el-row>
          <el-col :span="5">
            <div class="grid-content bg-purple">
              <el-input
                v-model="filterCondition.destAddr"
                placeholder="destination"
              ></el-input>
            </div>
          </el-col>

          <el-col :span="5">
            <div class="grid-content bg-purple-light">
              <el-date-picker
                type="date"
                placeholder="Choose a Date"
                v-model="filterCondition.date"
                style="width: 100%"
              >
              </el-date-picker>
            </div>
          </el-col>
          <el-col :span="5">
            <div class="grid-content bg-purple">
              <el-time-picker
                placeholder="Choose Time"
                v-model="filterCondition.time"
                style="width: 100%"
              >
              </el-time-picker>
            </div>
          </el-col>

          <el-col :span="5">
            <div class="grid-content bg-purple">
              <el-select
                v-model="filterCondition.numPeople"
                placeholder="Number of People"
              >
                <el-option label="1" value="1"></el-option>
                <el-option label="2" value="2"></el-option>
                <el-option label="3" value="3"></el-option>
                <el-option label="4" value="4"></el-option>
                <el-option label="5" value="5"></el-option>
                <el-option label="6" value="6"></el-option>
              </el-select>
            </div>
          </el-col>

          <el-col :span="4">
            <div class="grid-content bg-purple">
              <el-button type="primary" @click="searchRide">Submit</el-button>
            </div>
          </el-col>
        </el-row>
      </el-header>

      <el-main style="height: 100%">
        <div style="font-size: 20px">All Rides List</div>
        <el-table :data="tables">
          <el-table-column prop="date" label="date" width="140">
          </el-table-column>
          <el-table-column prop="time" label="time" width="150">
          </el-table-column>
          <el-table-column prop="destAddr" label="destination">
          </el-table-column>
          <el-table-column prop="numPeople" label="seats"> </el-table-column>
          <el-table-column prop="status" label="detail">
            <template slot-scope="scope">
              <router-link
                to="/ridedetail"
                @click.native="setCurrentRideDetail(scope.$index)"
                class="noDecoration"
              >
                more detail
              </router-link>
              </template>
          </el-table-column>
        </el-table>

          <el-divider ><i class="el-icon-info"></i></el-divider>
        <div style="font-size: 20px">Rides I Belong To</div>
        <el-table :data="ridesOwned">
          <el-table-column prop="date" label="date" width="140">
          </el-table-column>
          <el-table-column prop="time" label="time" width="150">
          </el-table-column>
          <el-table-column prop="destAddr" label="destination">
          </el-table-column>
          <el-table-column prop="numPeople" label="seats"> </el-table-column>
          <el-table-column prop="status" label="detail">
            <template slot-scope="scope">
              <router-link
                to="/ridedetail"
                @click.native="setCurrentRideDetail(scope.$index)"
                class="noDecoration"
              >
                more detail
              </router-link>
              </template>
          </el-table-column>
        </el-table>


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
import { loadRideList } from "../api/api.js";
import _ from "lodash";
export default {
  data() {
    return {
      tableData: [],
      filterCondition: {
        destAddr: "",
        date: "",
        time: "",
        numPeople: "",
      },
    };
  },
  methods: {
    setCurrentRideDetail(index) {
      this.$store.state.user.currentRideDetail.id        = this.tables[index].id
      this.$store.state.user.currentRideDetail.rideOwner = this.tables[index].rideOwner
      this.$store.state.user.currentRideDetail.destAddr  = this.tables[index].destAddr
      this.$store.state.user.currentRideDetail.driverID  = this.tables[index].driverID
      this.$store.state.user.currentRideDetail.isJoinable= this.tables[index].isJoinable
      this.$store.state.user.currentRideDetail.numPeople = this.tables[index].numPeople
      this.$store.state.user.currentRideDetail.otherInfo = this.tables[index].otherInfo
      this.$store.state.user.currentRideDetail.shareID   = this.tables[index].shareID
      this.$store.state.user.currentRideDetail.status    = this.tables[index].status
      this.$store.state.user.currentRideDetail.date      = this.tables[index].date
      this.$store.state.user.currentRideDetail.time      = this.tables[index].time
       
    },
    searchRide() {
      // TODO backend still need optimize
    },
  },
  mounted() {
    loadRideList().then(
      (response) => {
        if (response.data.length != 0) {
          this.tableData = _.cloneDeep(response.data);
        }
      },
      (err) => {
        alert(JSON.stringify(err.response.data));
      }
    );
  },
  computed: {
    tables() {
      const searchIsEmpty = _.every(this.filterCondition, _.isEmpty);
      if (searchIsEmpty) {
        return this.tableData;
      }
      return _.filter(this.tableData, (ride) => {
        console.log(ride.destAddr);
        return (
          (ride.destAddr
            .toLowerCase()
            .includes(this.filterCondition.destAddr.toLowerCase()) &&
            !_.isEmpty(this.filterCondition.destAddr)) ||
          (!_.isEmpty(this.filterCondition.numPeople) &&
            ride.numPeople == this.filterCondition.numPeople) ||
          (!_.isEmpty(this.filterCondition.date) &&
            ride.date.includes(this.filterCondition.date)) ||
          (!_.isEmpty(this.filterCondition.time) &&
            ride.time.includes(this.filterCondition.time))
        );
      });
    },
    ridesOwned(){
      //var rides = JSON.parse(JSON.stringify(this.tableData));
      return _.filter(this.tableData, (ride) => {
         // ride.shareID   === this.$store.state.user.id
        return (
          ride.rideOwner === this.$store.state.user.id ||
          ride.shareID   === this.$store.state.user.id
        );
      });
    }
  },
};
</script>