<template>
    <div class="">        <leftnav />
    <el-container style="height: 1000px; border: 1px solid #eee">

        <registercar />
    </el-container>
    </div>

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
import leftnav     from "../components/leftnav";
import registercar from "../components/registercar";

export default{
    data() {
        return {
        }
    }
}
</script>