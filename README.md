# ProjectLog

## 项目日志

本项目主要内容在于孤立词的评分以及其发音反馈，其中功能将逐步实现

由于需要部署到小程序，因此有域名www.kaldi-speech.cn

现在主要工作在于自己实现DTW与HMM-DNN，对比其效率
后期将选择使用Kaldi进行进一步的模型训练

目前主要方向以及进度

### 单词评分

实现方法

1. #### [基于DTW与标准语音进行对比]()
   #####[MFCC简单教程](http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/)
   #####[python_speech_features官方使用文档](https://python-speech-features.readthedocs.io/en/latest/)
   #####[使用Python_speech_features进行MFCC提取](https://www.jianshu.com/p/e32d2d5ccb0d)
   #####[MFCC的提取过程讲解]("https://blog.csdn.net/zouxy09/article/details/9156785")
   #####[动态时间规整]("https://www.cnblogs.com/zhizhan/p/4419066.html")    
   换行
2. #### [基于HMM+DNN的方法]()
   [HMM的简单说明](http://www.practicalcryptography.com/miscellaneous/machine-learning/hidden-markov-model-hmm-tutorial/)

### 句子评分

重点在于流畅度等