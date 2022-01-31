<template>
  <div class="app" style="height: 100%">
    <el-menu
      :default-active="activeIndex"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
    >
      <el-menu-item index="1"
        ><router-link to="/createuser" class="noDecoration" v-if="!loginStatus"
          >Create Account</router-link
        ></el-menu-item
      >
      <el-menu-item index="2"
        ><router-link to="/startride" class="noDecoration" v-if="loginStatus"
          >Start A Ride</router-link
        ></el-menu-item
      >

      <!-- <el-menu-item index="3"
        ><router-link to="/joinride" class="noDecoration" v-if="loginStatus"
          >Manage A Ride</router-link
        ></el-menu-item
      > -->

      <el-submenu index="3" v-if="loginStatus">
        <template slot="title">Manage Ride</template>
        <el-menu-item index="3-1">
             <el-button @click="hitOwnRides" style="border:none">My Own Rides</el-button>
        </el-menu-item>
        <el-menu-item index="3-2">
             <el-button @click="hitSharedRide" style="border:none">My Shared Rides</el-button>
        </el-menu-item>
        <el-menu-item index="3-3">
             <el-button @click="hitAvaRide" style="border:none">available Rides</el-button>
        </el-menu-item>
      </el-submenu>

      <el-submenu index="4" v-if="loginStatus">
        <template slot="title">Driver Only</template>
        <el-menu-item index="4-1"
          ><router-link to="/registercar" class="noDecoration"
            >Register/Edit A Car</router-link
          ></el-menu-item
        >
        <el-menu-item index="4-2"
          ><router-link to="/orderForDriver" class="noDecoration"
            >Orders' for Driver</router-link
          ></el-menu-item
        >
      </el-submenu>

      <el-menu-item index="5" v-if="loginStatus">
        <router-link to="/personinfo" class="noDecoration"
          >Profile</router-link
        ></el-menu-item
      >
      <el-menu-item index="6" v-if="loginStatus">
        <el-link target="_blank" @click="logout">Logout</el-link></el-menu-item
      >
    </el-menu>
    <div class="line"></div>

    <router-view />
  </div>
</template>

<script>
import { logoutUser } from "./api/api.js";
export default {
  name: "App",
  data() {
    return {
      // userlogin: this.$store.state.login,
      activeIndex: "/",
    };
  },
  methods: {
    handleSelect() {},
    logout() {
      this.$store.state.login = false;
      this.$store.state.user.id = "";
      logoutUser().then((response) => {
        this.$router.push("/");
      });
    },
    hitOwnRides(){
      this.$router.push('/myownorder')
    },
    hitSharedRide(){
      this.$router.push('/mysharedorder')
    },
    hitAvaRide(){
      this.$router.push('/availableorder')
    } 

  },
  computed: {
    loginStatus: function () {
      return this.$store.state.login;
    },
  },
};
</script>

<style>
.bgimg {
  background-image: url("./assets/seeing1.jpg");
}

.noDecoration {
  text-decoration: none;
}
html,
body,
#app {
  height: 100%;
}
</style>