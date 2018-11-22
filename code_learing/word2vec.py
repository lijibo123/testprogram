import gensim
import pandas as pd
model = gensim.models.Word2Vec.load('F:\word2vec\word2vec_wx')
print(pd.Series(model.most_similar('微信')))
#model.most_similar(u'马云')