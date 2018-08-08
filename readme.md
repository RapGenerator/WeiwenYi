# This is WeiwenYi's repo

## Model
### 2018/08/01
#### char-rnn-rap
* Simple demo to generate rap with char-rnn.

## Report
### 2018/08/01
* 完成RNN、LSTM、Word2Vec、Seq2Seq、BLEU等基础概念的学习。

### 2018/08/02
* 浏览从[网站](encore.ai)上寻找的一份代码，该demo主要是通过歌手的大量歌词通过简单的变种LSTM模型进行训练，生成该歌手风格的歌词。不涉及seq2seq模型但效果较好。LSTMModel.py代码中有一些值得借鉴的代码风格。[Git链接](https://github.com/dyelax/encore.ai)  
* 找到一份较好的demo，准备与大家一起学习。[Git链接](https://github.com/Disiok/poetry-seq2seq)  
* 老师开会，通过会上交流反思自身学习方法、进度上的不足，同时意识到团队合作的重要性。  
* 晚上组里开了讨论会，针对老师的问题进行讨论，包括RNN梯度推导，RNN存在的问题（梯度衰减、梯度爆炸）、RNN的隐藏状态所使用的场景、LSTM的结构原理（参与推导）、三个门的作用及计算方法、变种、GRU的结构与提升、LSTM激活函数替换问题。仍存在以下疑问：  
1. 梯度衰减应存在两个问题，一是sigmoid函数本身给cell带来的梯度消失，而是timestep很长的时候，即使是relu也存在梯度消失问题。  
1. LSTM激活函数换成relu是不是也会存在一些问题？  

### 2018/08/03
* 进行[代码](https://github.com/Disiok/poetry-seq2seq)的修改，出现模型json保存问题尚未调通。  
* 进入算法组，分配[论文](https://arxiv.org/abs/1610.09889)，配套[PPT](https://cs.uwaterloo.ca/~mli/Simon_Vera.pdf)。
* 该代码实现该论文，可以辅助论文学习

### 2018/08/06
* 阅读[论文](https://arxiv.org/abs/1610.09889)，上传阅读笔记至Report。
* 与老师进行项目进展与问题讨论。
* 与诗俊进行论文内容、主题生成idea讨论。  

### 2018/08/07
* 与诗俊进行论文内容、主题生成idea讨论。  
* 参与论文研讨会，讨论论文主题包括：
1. Topic Input Poem Generation
1. skip-thought
1. Beamsearch Score modified