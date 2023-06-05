from flask import Flask, render_template, request, make_response,jsonify,send_from_directory
import os
import json
import sys
from imageClass import ImageClass,getlabelName,getnotebook

app = Flask(__name__, static_url_path='/',
            static_folder='./../flask-dist', template_folder='./../flask-dist')
# 生成app对象  static_folder 设置资源位置  就是 js文件夹 css文件夹的目录   template_folder html文件位置
NOWDIR=os.path.dirname(sys.argv[0])

@app.route('/')
def index():
    return render_template('index.html')
# template_folder 设置的路径下的 index.html

@app.route('/image/<filename>')
def show_image(filename):
    return send_from_directory('image',filename)

@app.route('/newimage/<newfilename>')
def show_newimage(newfilename):
    return send_from_directory('newimage',newfilename)

@app.route('/handleImage', methods=['GET', 'POST'])
def handle_python_request():
    urls,newurls,new_class,new_prob,=[],[],[],[]
    files = request.files.getlist('Image')
    nowimagedir=os.path.join(NOWDIR,'image')
    newdir=os.path.join(NOWDIR,'newimage')
    csvpath=os.path.join(NOWDIR,'csv/labeldata.csv')
    for file in files:
        if file and allowed_file(file.filename):
            filename = file.filename
            if not os.path.exists(nowimagedir):
                os.makedirs(nowimagedir)
            filepath = os.path.join(nowimagedir, filename)
            if not os.path.exists(filepath):
                file.save(filepath)
            modelPath=os.path.join(NOWDIR,'best_model.pt')
            new=ImageClass(filepath,modelPath,newdir)
            max_class,max_prob=new.recognize_image()
            max_prob="{:.2%}".format(max_prob)
            max_class=getlabelName(csvpath,max_class)
            newurl='http://127.0.0.1:5000/newimage/'+filename
            url='http://127.0.0.1:5000/image/'+filename
            urls.append(url)
            newurls.append(newurl)
            new_class.append(max_class)
            new_prob.append(max_prob)
    return jsonify({'urls':urls,'newurls':newurls,'new_class':new_class,'new_prob':new_prob})

# 允许上传的图片类型
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    # 检查文件类型
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/deleteImage',methods=['DELETE'])
def delete_image():
    filenone=[]
    filenames=json.loads(request.get_data())
    filePath=os.path.join(NOWDIR,'image')
    newfilePath=os.path.join(NOWDIR,'newimage')
    if filenames['id']==1:
        file=os.path.join(filePath,filenames['names'])
        newfile=os.path.join(newfilePath,filenames['names'])
        if os.path.exists(file):
            os.remove(file)
            os.remove(newfile)
        else:
            filenone.append(filenames['names'])
    else:
        filenames=filenames['names']
        for filename in filenames:
            file=os.path.join(filePath,filename)
            newfile=os.path.join(newfilePath,filename)
            if os.path.exists(file):
                os.remove(file)
                os.remove(newfile)
            else:
                filenone.append(filename)
    if len(filenone):
        return jsonify({'filename':filenone})
    else:
        return "删除成功"

@app.route('/notebook',methods=['POST'])
def getnode():
    filepath=os.path.join(NOWDIR,'train.ipynb')
    content=getnotebook(filepath)
    return jsonify(content)

@app.route('/markdown')
def get_markdown_file():
    markdownPath=os.path.join(NOWDIR,'readme.md')
    with open(markdownPath,'r',encoding='utf-8') as f:
        markdown_content=f.read()
    return jsonify({'markdown_content':markdown_content})

if __name__ == '__main__':
    app.run(debug=True)
