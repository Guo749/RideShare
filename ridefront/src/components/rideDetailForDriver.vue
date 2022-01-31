<template>
  <el-container style="border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <el-row> </el-row>
      </el-header>

      <el-main style="height: 1000px">
        <el-descriptions
          class="margin-top"
          title="Ride Detail"
          :column="3"
          :size="size"
          border
        >
          <template slot="extra">
            <el-button type="info" size="small" :disabled="!hasRightToClaim" @click="claimOrder">Claim this order</el-button>
            <el-button type="success" size="small" :disabled="!hasRightMarkAsCompleted" @click="completeOrder">Mark As Completed</el-button>
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
            
            <el-tag type="danger" v-if="rideDetail.status == 3">completed</el-tag>
            <el-tag type="success" v-else-if="rideDetail.status == 2">confirmed</el-tag>
            <el-tag v-else>posted</el-tag>
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
import { getDriverByFk, getCarByFk, editride} from "../api/api.js";
import _ from "lodash";

export default {
  data() {
    return {
      size: "",
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
    };
  },
  methods: {
    init() {
      console.log("hasDriver: ", this.hasDriver)
      if (!!this.$store.state.user.currentDriverRideDeail.driverID) {
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
    claimOrder() {
        this.rideDetail.status = 2 
        this.rideDetail.driverID = this.$store.state.user.id
        editride(this.rideDetail.destAddr,
                this.rideDetail.date,
                this.rideDetail.time,
                this.rideDetail.numPeople,
                this.rideDetail.isJoinable,
                this.rideDetail.otherInfo,
                this.rideDetail.rideOwner,
                this.rideDetail.driverID,
                this.rideDetail.shareID,
                this.rideDetail.status,
                this.rideDetail.id
                ).then((response) => {
            this.$store.commit('setCurrentRideDetailForDriver', response.data)
            this.init()
            alert("successfully claim this order")
        }, (err) => {
            console.log(JSON.stringify(response.data))
        })
    },
    completeOrder() {
        this.rideDetail.status = 3
        editRide(this.rideDetail.destAddr,
                this.rideDetail.date,
                this.rideDetail.time,
                this.rideDetail.numPeople,
                this.rideDetail.isJoinable,
                this.rideDetail.otherInfo,
                ).then((response) => {
            this.$store.commit('setCurrentRideDetailForDriver', response.data)
            this.init()
            alert("successfully mark this order as completed")
        }, (err) => {
            console.log(JSON.stringify(response.data))
        })
    }
  },
  computed: {
    rideDetail() {
      return this.$store.state.user.currentDriverRideDeail
    },
    hasDriver() {
      return !!this.$store.state.user.currentDriverRideDeail.driverID;
    },
    hasRightToClaim() {
      return (!!this.$store.state.user.car.id) && (this.$store.state.user.currentDriverRideDeail.status == 1);
    },
    hasRightMarkAsCompleted() {
        return (!!this.$store.state.user.car.id) 
        && (this.$store.state.user.currentDriverRideDeail.status == 2)
        && (this.$store.state.user.currentDriverRideDeail.driverID == this.$store.state.user.id)
    }
  },
  watch: {
    hasDriver: function(newVal, oldVal) {
        this.init()
    }
  },
  mounted() {
      setTimeout(() => {
          this.init()
      }, 500)
  },
};
</script>