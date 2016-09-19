# **Inquisit_Lab_4 初体验**
---
### Inquisit 使用类似于 HTML 的标签语言进行编程，在这一节我们将初次学习使用这种语言进行编程，编制你的第一个实验程序。如果你是编程圣手，之前惯用HTML语言，那么Inquisit 对于你来说是小菜一碟；如果你之前根本没接触过编程，Inquisit 也一点儿不难，正好可以练手。那我们的就开始吧！

### 编程就是像画画，首先你心中需要胸有成竹，编程只是用画笔将心中的图景画出来。如果没有具体的图景，编程没啥用处。
---
*Inquisit Lab 使用的是脚本语言，即一个普通的文本文件，可以采用任何编辑器中进行编辑，最后保存为后缀为.exp的文件即可。对于已存在的.exp 文件，双击这个文件，Inquisit Lab 就会自动运行脚本程序，并自动在实验程序对应文件夹中生成一个与文件名同名的.dat文件，记录实验数据；选择打开方式打开，将进入编辑模式，可以修改文件内容。在Inquisit 运行过程中，如果要强制退出，请按 Ctrl + Q.* 
---
### 现在打开Inquisit Lab, 一个空白的IDE会呈现在你的面前（用图片简单的介绍一下IDE各个模块，菜单栏已经对应的功能），如果让Inquisit Lab 运行起来实现实验功能呢？

- 首先，你需要自上而下的思考，并作出几个决定。你的实验目的是什么，应该采用什么样的实验范式。（举例：假设你的实验目的是看被试是否存在一种对鲜花和蜘蛛的内隐偏好，一种可行的实验范式就是IAT范式，可以采用图片，也可以采用文字。为了简单起见，在第一个实验程序中，我们采用文字版本）

- 其次，你需要自下而上的思考，试着自下而上的回答以下问题。

* **刺激材料**：你需要什么样的刺激材料？什么类别？（举例：IAT 需要的刺激材料，可以选用文字材料，4个类别，分别是鲜花类、蜘蛛类、积极词汇、消极词汇，每个类别10个刺激）

* Trials: What kind of trials do you need? What does a trial look like? What is the order and timing of the stimuli? What kind of responses can a participant give? When is a response the right one?

* What happens if the participant responds incorrectly?

* Blocks: How are the trials ordered in blocks? What are the instructions for each block?

* Experiment: How are the blocks ordered? How does this depend on conditions? How are conditions selected?

On each level of the bottom-up thought process there is an Inquisit counterpart that you need to program. I recommend that when you program, you start out programming the experiment in this same bottom-up order.




