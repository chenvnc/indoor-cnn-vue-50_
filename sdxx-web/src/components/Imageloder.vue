<template>
  <div class="main">
    <!-- 预览 -->
    <el-empty id="empty" :image="previewPaths[index - 1]" :image-size="200" :description="imageName[index - 1]">
      <el-button type="primary" @click="imageLoad">
        上传图片
        <el-icon class="el-icon--right">
          <Upload></Upload>
        </el-icon>
      </el-button>
      <Delete class="all-delete" @click="deleteAllImage" v-if="index > 0 ? true : false"></Delete>
      <input type="file" id="file" style="display: none;" ref="files" @change="upload" multiple>
    </el-empty>
    <!-- 图片 -->
    <div>
      <transition-group name="list" tag="ul">
        <div v-for="(previewPath, idx) in previewPaths" :key="previewPath" class="demo-image-div">
          <!-- 原图 -->
          <div>
            <el-card :body-style="{ padding: '0px' }" class="demo-inner-container" shadow="hover">
              <el-image class="demo-image" :src="previewPath" fit="cover" />
              <div style="padding: 10px">
                <span>
                  原图
                </span>
                <div class="bottom">
                  <time class="time">{{ currentDate }}</time>
                  <p>{{ imageName[idx] }}</p>
                </div>
              </div>
            </el-card>
          </div>
          <!-- 归一化处理 -->
          <div>
            <el-card :body-style="{ padding: '0px' }" class="demo-inner-container" shadow="hover">
              <el-image class="demo-image" :src="newpreviewPaths[idx]" fit="cover" />
              <div style="padding: 10px">
                <span>处理</span>
                <div class="bottom">
                  <time class="time">{{ currentDate }}</time>
                  <p>{{ imageName[idx] }}</p>
                </div>
              </div>
            </el-card>
          </div>
          <!-- 结果 -->
          <div class="demo-inner-container">
            <p>图片{{ newProb[idx] }}为{{ newClass[idx] }}</p>
          </div>
          <!-- 删除 -->
          <Delete class="demo-delete" @click="showConfirmDialog(idx)"></Delete>

        </div>
      </transition-group>
      <el-divider />
    </div>
    <!-- 回到顶部 -->
    <el-backtop :right="100" :bottom="100" />
  </div>
</template>
<script>
import { ref } from 'vue'
import { Upload, Delete } from '@element-plus/icons-vue'
import { getmessage, messagebox, http } from '../js/message'
export default {
  name: 'classify',
  components: {
    Upload: Upload,
    Delete: Delete,
  },
  data() {
    return {
      previewPaths: [],
      index: 0,
      imageName: [],
      newpreviewPaths: [],
      newClass: [],
      newProb: [],
      currentDate: ref(new Date())
    }
  },
  methods: {
    // 点击上传图片
    imageLoad() {
      this.$refs.files.click();
    },
    // 上传图片
    async upload(event) {
      var fileObj = event.target.files;
      length = fileObj.length
      this.index += length
      const formData = new FormData();
      for (let i = 0; i < length; i++) {
        this.imageName.push(fileObj[i].name)
        formData.append('Image', fileObj[i]);
      }
      if (length > 0) {
        const url = '/handleImage'
        await http('post', url, formData)
          .then((response) => {
            let urls_length = response.data.urls.length
            for (let i = 0; i < urls_length; i++) {
              this.previewPaths.push(response.data.urls[i])
              this.newpreviewPaths.push(response.data.newurls[i])
              this.newClass.push(response.data.new_class[i])
              this.newProb.push(response.data.new_prob[i])
            }
            for (let i = 0; i < urls_length; i++) {
            }
            getmessage('success', '上传成功')
          })
          .catch((error) => {
            this.index -= length
            for (let i = 0; i < length; i++)this.imageName.pop()
            getmessage('error', '上传失败')
            console.log(error);
          });
      }
    },
    // 删除单张图片
    async showConfirmDialog(idx) {
      await messagebox('是否删除？')
        .then(() => {
          const url = '/deleteImage'
          const data = JSON.stringify({ names: this.imageName[idx], id: 1 })
          const headers = ['application/json;charset=utf-8']
          http('delete', url, data, headers)
            .then((response) => {
              this.previewPaths.splice(idx, 1);
              this.imageName.splice(idx, 1);
              this.newpreviewPaths.splice(idx, 1)
              this.newClass.splice(idx, 1)
              this.newProb.splice(idx, 1)
              this.index -= 1;
              getmessage('success', response.data)
            }).catch((error) => {
              getmessage('error', '删除失败')
              console.log(error)
            })
        }).catch((error) => {
          getmessage('info', '删除操作撤销')
          console.log(error)
        });
    },
    // 删除全部图片
    async deleteAllImage() {
      if (this.index) {
        await messagebox('确认删除全部？')
          .then(() => {
            const url = '/deleteImage'
            const data = JSON.stringify({ names: this.imageName, id: 2 })
            const headers = ['application/json;charset=utf-8']
            http('delete', url, data, headers)
              .then((response) => {
                for (let i = 0; i < this.index; i++) {
                  this.previewPaths.pop()
                  this.imageName.pop()
                  this.newpreviewPaths.pop()
                  this.newClass.pop()
                  this.newProb.pop()
                }
                this.index = 0;
                getmessage('success', response.data)
              }).catch((error) => {
                getmessage('error', '删除失败')
                console.log(error)
              })
          }).catch(() => {
            getmessage('info', '删除操作撤销')

          });
      }
      else getmessage('info', '没有文件')
    },

  },
}
</script>
<style scoped>
pre,
span {
  color: #337ecc;
  font-size: large;
  font-family: 'Helvetica Neue', Helvetica;
  text-shadow: 0 0 1px rgba(0, 0, 0, 0.526);
}
.main {
  position: relative;
  display: flex;
  flex-direction: column;
}
.all-delete {
  cursor: pointer;
  position: absolute;
  width: 25px;
  height: 25px;
  opacity: 0.5;
}

.demo-image-div {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  position: relative;
  box-shadow: 0 0px 3px #606266;
  border-radius: 5px;
  margin-bottom: 10px;
  /* background-color: #F2F6FC; */
}

.demo-inner-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}


.demo-inner-container span {
  writing-mode: vertical-lr;
}

.demo-image {
  width: 310px;
  height: 250px;
  transform: scale(1);
  transition: transform 0.5s ease; /* 添加过渡效果 */
}

.demo-image:hover{
  transform: scale(1.5);
}

.time {
  font-size: 10px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  flex-direction: column-reverse;
  align-items: flex-start;
}

.demo-delete {
  cursor: pointer;
  position: absolute;
  width: 25px;
  height: 25px;
  top: 20px;
  right: 20px;
  opacity: 0.5;
}

.demo-delete:hover,
.all-delete:hover {
  transition: all 0.5s ease;
  opacity: 1;
}

.demo-delete:active,
.all-delete:active {
  transition: all 0.2s ease;
  transform: scale(0.8, 0.8);
}

.list-move,
.list-enter-active,
.list-leave-active {
  transition: all 0.8s ease-in-out;
}

.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: scale(0.01)
}

.list-leave-active{
  position: absolute;
}
</style>
