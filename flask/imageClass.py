import torch
import torch
import os
import nbformat
from torch import nn
import numpy as np
import pandas as pd
from PIL import Image
from torchvision import transforms

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            # 224x224x3
            nn.Conv2d(3,64,5,2,2),
            nn.MaxPool2d(3,2,1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(64,64,3,1,1),
            nn.MaxPool2d(3,1,1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            # 56x56x64
            nn.Conv2d(64,128,3,2,1),
            nn.MaxPool2d(3,1,1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(128,128,5,1,2),
            nn.MaxPool2d(3,1,1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            #28*28*128
            nn.Conv2d(128,256,3,2,1),
            nn.MaxPool2d(3,1,1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(256,256,5,2,2),
            nn.MaxPool2d(3,1,1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            #7*7*256
            nn.AvgPool2d(7),
            nn.Flatten(),
            nn.Linear(256, 67),
        )

    def forward(self, x):
        x = self.conv1(x)
        return x

class ImageClass:
    def __init__(self,imgPath,modelPath,saveDir):
        self.imgPath=imgPath
        self.modelPath=modelPath
        self.saveDir=saveDir
        #创建保存目录
        os.makedirs(saveDir,exist_ok=True)

    def recognize_image(self):
        # 加载模型
        model=CNN()
        model.load_state_dict(torch.load(self.modelPath,map_location=torch.device('cpu')))
        model.cpu()
        model.eval()
        transform = transforms.Compose([
            transforms.Resize((224,224)),  # 将图像缩放为224x224大小
            transforms.ToTensor(),  # 将图像转化为tensor
            transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])  # 归一化处理
        ])
        img=Image.open(self.imgPath)
        # 将图像转换
        img=transform(img).unsqueeze(0).cpu()
        with torch.no_grad():
            output = model(img)
            result = torch.nn.functional.softmax(output[0], dim=0)
            max_prob, max_class = torch.max(result, dim=0)

        save_path=os.path.join(self.saveDir,os.path.basename(self.imgPath))
        img=img.cpu().squeeze().numpy().transpose((1,2,0))
        img=Image.fromarray((img*255).astype(np.uint8))
        img.save(save_path)
        return int(max_class.item()), float(max_prob.item())

def getlabelName(filepath,key):
    df=pd.read_csv(filepath,header=None,names=['num','label'])
    for i in range(len(df)):
        if df['num'][i]==key:
            return df['label'][i]
        
def getnotebook(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    cells_content=[]
    for cell in nb.cells:
      if cell.cell_type == 'code':
        # 代码单元格
        cells_content.append({'code':cell.source})
      elif cell.cell_type == 'markdown':
        # Markdown 单元格
        cells_content.append({'markdown':cell.source})
      if cell.cell_type=='code' and cell.outputs:
          cells_content.append({'output':cell.outputs})
    return cells_content