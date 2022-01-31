<template>
  <el-container style="border: 1px solid #eee">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    </el-aside>

    <el-container>
      <el-header style="text-align: right; font-size: 12px">
        <el-row> </el-row>
      </el-header>

      <el-main style="height: 1000px">
        <el-dialog title="Edit User" :visible.sync="dialogFormVisible">
          <el-form :model="userForm" ref="userForm" label-position="left">
            <el-form-item label="username" prop="username">
              <el-input v-model="userForm.username"></el-input>
            </el-form-item>
            <el-form-item label="email" prop="email">
              <el-input v-model="userForm.email"></el-input>
            </el-form-item>
          </el-form>

          <el-button type="primary" size="small" @click="editPerson"
            >Submit</el-button
          >
        </el-dialog>

        <el-descriptions
          class="margin-top"
          title="Personal Infomation"
          :column="3"
          border
        >
          <template slot="extra">
            <el-button type="primary" size="small" @click="toggle">
              Edit
            </el-button>
          </template>

          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-user"></i>
              Username
            </template>
            {{ this.$store.state.user.username }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-mobile-phone"></i>
              Email Addresss
            </template>
            {{ this.$store.state.user.email }}
          </el-descriptions-item>
        </el-descriptions>

        <el-descriptions class="margin-top" title="Car Info" :column="3" border>
          <template slot="extra">
            <el-button type="primary" size="small" @click="editCar"
              >Edit</el-button
            >
          </template>

          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-user"></i>
              Type
            </template>
            {{ this.$store.state.user.car.type }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-mobile-phone"></i>
              License Number
            </template>
            {{ this.$store.state.user.car.licensePlateNumber }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-location-outline"></i>
              capacity
            </template>
            {{ this.$store.state.user.car.capacity }}
          </el-descriptions-item>

          <el-descriptions-item>
            <template slot="label">
              <i class="el-icon-office-building"></i>
              Other Info
            </template>
            {{ this.$store.state.user.car.otherInfo }}
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
import { editUser, logoutUser } from "../api/api.js";
export default {
  data() {
    return {
      dialogFormVisible: false,
      userForm: {
        username: "",
        email: "",
      },
    };
  },

  methods: {
    editCar: function () {
      this.$router.push("/registercar");
    },
    toggle: function () {
      this.dialogFormVisible = true;
    },
    editPerson: function () {
      console.log(this.$store.state.user.username);
      editUser(
        this.userForm.username,
        this.userForm.email,
        this.$store.state.user.id,
      ).then((response) => {
        this.$store.state.user.username  = this.userForm.username
        this.$store.state.user.email     = this.userForm.email
        this.$router.push('/startride')
      });
    },
  },
};
</script>