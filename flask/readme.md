## 配置

**Python:**`flask pytorch torchvision pillow nbformat pandas`或者创建新的虚拟环境把`flask/requirements.txt`直接`pip install -r requirements.txt`

**vue:** 终端进入`sdxx-web/`文件夹直接输入`npm install`自动安装依赖

## 文件结构
有三个文件夹分别为`flask,flask-dist,sdxx-web`
```
flask 后端文件夹
    --__pycache__ 不重要文件夹

    -- csv 存储着csv格式的数据

    -- image 存储上传到后端的图像文件

    -- newimage 存储经转换后的图像文件

    -- best_model.pt 文件为保存最好状态的模型

    -- imageClass.py 文件为主要调用的函数和Class

    -- readme.md 说明性文件

    -- requirements.txt 项目所需的包

    -- run.py 文件为主要运行程序

    -- train.ipynb 文件为训练cnn模型的代码

flask-dist  为前端打包后的静态文件夹

sdxx-web  前端vue项目文件夹
    -- node_modules 下载的vue前端包所在

    -- src 为主要文件所在
        --assets 存储着前端所用到的资源(图片等)

        --components 前端代码所在处称之为组件

        --js js文件前端可用调用

        --router 路由配置所在

        --App.vue 首页面代码

        --main.js 核心文件，负责启动整个Vue应用程序并挂载Vue实例

        --style.css 样式文件
    
    -- index.html Web页面的入口点

    -- vite.config.js Vue.js应用程序的配置文件
```

**运行：**
* `/flask`文件夹下的`run.py`文件直接运行,浏览器打开终端显示的地址，也可直接显示前端页面并成功响应(flask以连接静态文件)
* 也可以运行完`run.py`文件后不打开它显示的地址,在终端进入`/sdxx-web`文件夹输入命令`npm run dev`进行vue前端打开,也能实现显示页面并成功显示

## 前端打包
需进`/sdxx-web/src/js/message.js`修改`http`函数里的`url`就可以实现前端打包并可以连后端