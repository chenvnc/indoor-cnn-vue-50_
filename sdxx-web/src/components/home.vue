<template>
  <div class="common-layout">
        <el-header class="head">
            <el-menu router :default-active="$route.path"
             class="el-menu-demo" 
             mode="horizontal" 
             :ellipsis="false"
             >
              <router-link to="/" class="link">
                <el-menu-item>
                  首页
                </el-menu-item>
              </router-link>

              <router-link to="/outcome" class="link">
                <el-menu-item>
                  过程
                </el-menu-item>
              </router-link>

              <el-sub-menu index="about">
                <template #title>关于</template>

                <router-link to="/author" class="link">
                  <el-menu-item >作者</el-menu-item>
                </router-link>
                <router-link to="/resource" class="link">
                  <el-menu-item>指南</el-menu-item>
                </router-link>

                <router-link to="/more" class="link">
                  <el-menu-item>
                    <el-icon>
                      <More />
                    </el-icon>
                  </el-menu-item>
                </router-link>

              </el-sub-menu>
            </el-menu>
        </el-header>
        <el-main class="main">
          <router-view v-slot="{ Component }">
            <keep-alive :include="'*'">
              <component :is="Component" :key="$route.fullPath"></component>
            </keep-alive>
          </router-view>
        </el-main>
  </div>
</template>
<script lang="ts" setup>
import { More } from '@element-plus/icons-vue'
</script>

<style>
.common-layout {
  display: flex;
  flex-direction: column;
}

.head {
  position: fixed;
  z-index: 1000;
  width: 100%;
  top:0;
}
.main {
  margin-top: 57.6px;
  position: relative;
}
.el-menu-demo {
  display: flex;
  justify-content:center;
}

.link {
  text-decoration: none;
  font-size: medium;
}
</style>
