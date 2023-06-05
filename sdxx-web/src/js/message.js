import { ElMessage, ElMessageBox } from 'element-plus';
import axios from 'axios'
export function getmessage(type, data) {
  ElMessage({
    type: type,
    message: data
  })
}

export function messagebox(message) {
  return ElMessageBox.confirm(message, '提示', {
    confirmButtonText: '确认',
    cancelButtonText: '取消',
    type: 'warning'
  });
}
export function http(method, url, data=null, headers = null) {
  // url='/api'+url//打包时注释
  const axiosConfig = {
    method: method,
    url: url,
    data: data?data:null,
    headers:headers?{contentType:headers[0]}:null
  }
  return axios(axiosConfig)
}