# 本程序是基于jieba分词工具处理文档及其内容
# 每篇文章一行文本
from jieba.analyse import *
import jieba
import numpy as np
import jieba.posseg as psg
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

'''
with open('abstract.txt','r') as f:
    con = f.read()
for keyword, weight in extract_tags(con, topK=10,withWeight=True):
# for keyword,weight in textrank(con, topK = 10,withWeight=True):
    print('%s %s' % (keyword,weight))
'''
# 这里存储常用词汇的列表
stop_words = []
X,Y = ['\u4e00', '\u9fa5']
word_str = []
# 文档的存储路径
path = ''
with open('word.txt') as file:
    content = file.readlines()  # 读取文件内容
    for line in content:
        word_cut = jieba.lcut(line)
        # word = [i for i in word_cut if len(i) >= 2 and X <= i <= Y and i not in stop_words]
        word = [i for i in word_cut if len(i) >= 2 and X <= i <= Y]
        word_str.append(' '.join(word))
    word1 = ['']
    print(word_str)
    vectorizer = CountVectorizer()  # 计算词频矩阵
    word_matrix = vectorizer.fit_transform(word_str)
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(word_matrix)

    words = vectorizer.get_feature_names()
    words = np.array(words)
    word_weight = tfidf.toarray()
    # 关键词语提取

    for i in range(len(word_weight)):
       sorted_weight = np.argsort(-word_weight[i])
       #for j in range(len(words)):
       print('第%d篇文档的关键词：\n' % i )
       for j in sorted_weight:
          print(words[j],word_weight[i][j])


