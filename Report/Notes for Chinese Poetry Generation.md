# "Chinese Poetry Generation with Planning based Neural Network" 阅读笔记

## 方法
- 诗歌生成方法
	- 输入：写作意图（可以是单词、句子、文档）
		- 将输入转换成N个关键词，每一个关键词代表每一行的sub-topic
		- 如果用户的输入太长，提取最重要的N个单词
		- 关键词序列与原始输入顺序保持一致
	- 输出：诗歌
		- 每一行依据 该行前的每句诗歌与当前主题 进行生成
	- 方法：Poem Planning and Poem Generation
		- Poem Planning
			- 关键词提取TextRank: 基于PageRank的一种graph-based ranking算法，每一个候选词为图中的节点，边权重代表coocurrence(两个单词的共现数量)  
			- 关键词扩展:  
				RNNLM-based:根据之前的关键词序列预测。在每一行中根据TextRank分数排序单词，最高分数作为该行的关键词。  
				Knowledge-based：给定关键词，找到一些能描述和解释该关键词的方法。  
				使用了以下候选关键词：
				1. window_size[-5,5]？
				1. adj/noun
				1. 在诗歌的训练语料库中
		- Poem Generation
			- 输入：上一次输出的诗歌与当前主题
			- 模型：seq2seq(Bi-directional GRU)+attention
				- 关键词部分双向RNN:输入为关键词<EOS>，采用前后向RNN的最后一个隐状态组合成主题隐状态.
				- 诗歌生成部分双向RNN:组合主题隐状态与诗歌生成部分的语义隐状态
				- 第一行没有上一行，所以诗歌生成部分的双向RNN不存在，语义隐状态为主题隐状态
## 实验
- 数据集  
	1. 4行诗，每行5/7字		
	1. 76859首诗，随机选择2000首诗作为验证集，2000首测试集，剩下的训练集
- 分词：基于CRF分词
- TextRank score:最高的作为该行的关键词
- 关键词扩展
	- 使用72859个关键词训练RNNLM-based模型
	- 使用百度百科和维基百科作为knowledge的其他来源训练knowledge-based模型
- 训练
	1. AdaDelta algorithm
    1. 最终模型选择基于验证集的perplexity
- 评估
	- Metrics
	BLEU/METEOR
	- Standards
	
| standard | explanation |
|----------|------|
| poeticness | 诗歌是否遵循rhyme押韵和语调需求 |
| fluency | 诗歌是否读起来平稳和流畅|
| coherence | 诗歌的每一行是否一致与连贯 |
| meaning | 诗歌是否有一个特定的含义和意境 |




