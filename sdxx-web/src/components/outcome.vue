<template>
  <div>
    <el-main class="main">
      <div class="main-content">
        <h2 id="guocheng">实验过程</h2>
        <div v-for="(cell, index) in cells" :key="index"
          :class="{ 'content-frame': true, 'output': cell.output, 'markdown': cell.markdown }">
          <pre v-if="cell.code">{{ cell.code }}</pre>
          <div v-if="cell.markdown" v-html="marked(cell.markdown)" :id="'markdown-' + index"></div>
          <pre v-if="cell.output">{{ cell.output[0].text }}</pre>
        </div>
        <el-divider border-style="dashed" />
        <h2 id="jieguo">实验结果</h2>
        <div class="content-frame markdown">
          <div id="loss-1">损失率plt图像如下:</div>
          <img src="../assets/loss.png" alt="loss">
          <div class="little">
            从上述'loss plot'图像可以看到Train曲线一直往下降,15次迭代后趋于稳定,
            虽然训练集的损失率降到了很低的地位置,但对于验证集和测试集没有什么帮助,
            而且还让Validation曲线和Test曲线升高,损失率增大。Validation曲线和Test曲线
            在6-13次之间的损失达到最低,而前后的损失率就不太理想了。
          </div>
          <el-divider border-style="dashed" />

          <div id="acc-1">准确率曲线如下:</div>
          <img src="../assets/acc.png" alt="acc">
          <div class="little">
            从上述准确率曲线'Accuracy Curve'可以看到训练集在每次迭代正确率都有
            很大的提升,但对于验证集和测试集来说,前7次迭代都是很大的提升,但在后面的
            迭代次数大于7,它们的正确率在50%左右徘徊,在第二十次时还回落,说明迭代次数
            多不一定会增长,所以需要在某一个最大值保存模型以便识别分辨率最高。
          </div>
          <el-divider border-style="dashed" />

          <div id="model-1">模型迭代:</div>

          <div class="little">
            模型1:对于卷积层、池化层和全连接层等不怎么熟悉,虽说不是真正意义上的第一代模型,
            但这模型还是获得较大的进步的,测试集正确率达到了37%,要说之前的模型都没上到过20%。
          </div>
          <img src="../assets/1.png" alt="1">
          <el-divider border-style="dashed" />

          <div class="little">
            模型2:这个模型相比之前的模型卷积层更少一层,添加了验证集,其他的不怎么变,虽说迭代次数变为20了,
            但这个模型还是获得不错的效果的,测试集和验证集正确率都上了40%。
          </div>
          <img src="../assets/2.png" alt="2">
          <el-divider border-style="dashed" />

          <div class="little">
            模型3:相对于前两个模型,图像缩放大小从256x256到224x224,全连接层也变为一层,
            卷积层为4层,但出来的效果就不是很好。
          </div>
          <img src="../assets/3.png" alt="3">
          <el-divider border-style="dashed" />

          <div class="little">
            模型4:相对于前面的模型,此模型效果还是不怎么好。
          </div>
          <img src="../assets/4.png" alt="4">
          <el-divider border-style="dashed" />

          <div class="little">
            最终代:可以看到卷积层有6层,其他也是,最后再把所有的像素AvgPool2d平均最后变成1,
            这代就相对于前面来说最大的不同,最后测试集和验证集正确率都上到了50%。
          </div>
          <img src="../assets/5.png" alt="5">
          <el-divider border-style="dashed" />

        </div>
        <h2 id="outcome-1">实验结论</h2>
        <div class="little">
          卷积神经网络(Convolutional Neural Network,CNN)是一种广泛应用于计算机视觉领域的深度学习模型。
          在使用 CNN 模型进行图像识别、目标检测等任务时，
          模型的精度和泛化能力取决于训练数据的质量和数量，以及模型优化算法的选择和调整。
        </div>
        <div class="little">
          在实验中，通常需要准备大量的带有标签的数据集，将其分为训练集、验证集和测试集，并使用 CNN 模型对数据进行训练和验证。
          模型的训练过程通常需要进行多次迭代，每次迭代中都会计算损失函数的值，在梯度下降算法的指导下逐步更新模型参数。
          当损失函数收敛时，说明模型已经完成了训练，可用于预测和测试新的数据。
        </div>
        <div class="little">
          在我的实验中，我使用了基于 CNN 训练的模型来进行图像分类任务。我先下载了一个大型图像数据集,其中包含了多个不同类别的图像样本。然后,我将数据集随机分成了训练集、验证集和测试集,比例为8:1:1。
          在多次实验的过程中,我调整了模型中的参数和超参数,并逐步优化了模型的精度和泛化能力。最终,我得到了一个在测试集上表现良好的模型,可以正确识别不同类别的图像，并且对新数据的预测效果也比较稳定。
        </div>
        <div class="little">
          通过这次实验，我深刻体会到了深度学习模型训练的复杂性和挑战性。在模型的训练过程中，需要针对具体的任务和数据集进行选型和调试，同时还需要高效地处理大量的数据和特征。
          此外，优化算法的选择和超参数的调整也非常关键，可以直接影响模型的精度和泛化能力。
          通过不断尝试和改进，我不仅掌握了卷积神经网络的基本原理和训练流程，还更加清晰地认识到了深度学习技术的重要性和应用前景。
        </div>
      </div>
      <el-aside class="aside">
        <div>
          <div @click="go('#guocheng')" class="link">实验过程</div>
          <template v-for="(cell, index) in cells">
            <div :key="index" v-if="cell.markdown" @click="go('#markdown-' + index)" class="link link-little">
              {{ cell.markdown.substr(6, 6) }}...
            </div>
          </template>
          <div @click="go('#jieguo')" class="link">实验结果</div>
          <div class="link link-little" @click="go('#loss-1')">损失率</div>
          <div class="link link-little" @click="go('#acc-1')">准确率</div>
          <div class="link link-little" @click="go('#model-1')">模型迭代</div>
          <div class="link" @click="go('#outcome-1')">实验结论</div>
        </div>
        <div></div>
      </el-aside>
    </el-main>
    <!-- 回到顶部 -->
    <el-backtop :right="100" :bottom="100" />
  </div>
</template>
<script>
import { http } from '../js/message'
import { marked } from 'marked'
export default {
  data() {
    return {
      cells: [],
    }
  },
  created() {
    this.fetchNotebookCells('/notebook')
  },
  methods: {
    fetchNotebookCells(url) {
      http('post', url)
        .then((response) => {
          this.cells = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    marked(content) {
      marked.setOptions({
        headerIds: false,
        mangle: false,
      })
      return marked(content)
    },
    go(selector) {
      document.querySelector(selector).scrollIntoView({
        behavior: "smooth"
      });
    }
  }
}
</script>
<style scoped>
img {
  width: 800px;
}

.main {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 0;
  margin: 0;
}

.main-content {
  width: 80%;
}

.aside {
  right: 0;
  width: 20%;
  position: fixed;
}

.main-content,
.aside {
  display: flex;
  flex-direction: column;
  padding: 2%;
}

.content-frame {
  box-shadow: 0 0 5px rgb(207, 232, 252);
  border: 1px solid rgb(207, 232, 252);
  border-radius: 5px;
  padding: 2%;
  background-color: rgb(241, 243, 245);
  line-height: 25px;
  display: flex;
  flex-direction: column;
}

pre {
  color: #212121;
  white-space: pre-wrap;
  font-family: 'Helvetica Neue', Helvetica;
}

.markdown {
  font-size: 20px;
  background-color: white;
  box-shadow: none;
  border: none;
}

.output {
  box-shadow: none;
  border: none;
  background-color: white;
  font-size: 12px;
  line-height: 20px;
}

.little {
  text-indent: 2em;
  line-height: 1.7;
  padding-right: 25%;
  font-size: 16px;
}

.link {
  cursor: pointer;
  color: rgb(154, 154, 162);
  font-size: 18px;
}

.link-little {
  font-size: 15px;
  padding: 2%;
  line-height: 20px;
  margin-left: 3%;
  white-space: pre-wrap;
}

.link:hover {
  color: #409EFF;
}

@media(max-width:900px) {
  .aside {
    display: none;
  }

  img {
    width: 300px;
  }
}
</style>