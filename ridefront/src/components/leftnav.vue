<template>
<!-- <el-container style="height: 1000px; border: 1px solid #eee"> -->
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['1', '3']">

<!-- ///////////////// item 1 ////////////////////////////////////////////////// -->

      <el-submenu index="1">
        <template slot="title"><i class="el-icon-message"></i>Start A Ride</template>
      </el-submenu>

<!-- ////////////////// item 2 ////////////////////////////////////////////////// -->

      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>Join A RIde</template>
      </el-submenu>

<!-- ////////////////// item 3 ////////////////////////////////////////////////// -->

      <el-submenu index="3">
        <template slot="title"><i class="el-icon-setting"></i>Claim A Ride</template>
        <el-menu-item-group>
          <el-menu-item index="3-1">Register A Car</el-menu-item>
          <el-menu-item index="3-2">Find Orders</el-menu-item>
        </el-menu-item-group>
      </el-submenu>


    </el-menu>
  </el-aside>
  
<!-- </el-container> -->

    
</template>
<style>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  
  .el-aside {
    color: #333;
  }
</style>

<script>
  export default {
    data() {
      const item = {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      };
      return {
        tableData: Array(20).fill(item)
      }
    }
  };
</script>