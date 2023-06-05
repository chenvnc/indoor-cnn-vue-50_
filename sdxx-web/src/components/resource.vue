<template>
  <el-main>
    <div v-if="data?true:false" v-html="marked(data)"></div>
  </el-main>
</template>
<script>
import { marked } from 'marked';
import { http } from '../js/message';
export default{
  data(){
    return{
      data:undefined
    }
  },
  created() {
    http('get','/markdown')
    .then(response=>{
      this.data=response.data.markdown_content
    })
    .catch(error=>{
      console.log(error)
    })
  },
  methods:{
    marked(content) {
      marked.setOptions({
        headerIds: false,
        mangle: false,
      })
      return marked(content)
    },
  }
}
</script>
<style scoped>
div {
  font-size: 16px;
  padding: 2%;
  line-height: 15px;
  font-family: 'Helvetica Neue', Helvetica;
}
</style>