<template>
  <el-container>
    <el-header>
      <div>
        <div>
          <el-avatar :icon="UserFilled" />
        </div>
      </div>
    </el-header>
    <el-aside width="200px">
    </el-aside>
    
  </el-container>
</template>
<script setup>
import { UserFilled } from '@element-plus/icons-vue'
</script>