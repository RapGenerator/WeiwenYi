import pandas as pd
import sys
import random
import gensim
import numpy as np

#dict_topic
dict_topic = {0.0: '',
              1.0: '亲情', 1.1: '痛苦',
              2.0: '爱情', 2.1: '青春', 2.2: '失恋',
              3.0: '友情', 3.1: '兄弟', 3.2: '背叛',
              4.0: '成功', 4.1: '坚持', 4.2: '告诫',
              5.0: '失败', 5.1: '迷茫', 5.2: '艰难不易',
              6.0: '过去', 6.1: '回忆', 6.2: '成长',
              7.0: '将来',
              8.0: '金钱', 8.1: '物欲',
              9.0: '努力',
              10.0: 'diss', 10.1: '讨厌', 10.2: '憎恶', 10.3: '虚伪',
              11.0: '积极',
              12.0: '生活',
              13.0: '中国风',
              14.0: '耍帅'}

# Load Model
model = gensim.models.Word2Vec.load("word2vec/word2vec_wx")

def Topic_Generation(prime):

    # change theme
    theme_class = list(dict_topic.values())
    del theme_class[0]
    theme_class[13] = '艰难'
    theme_class[27] = '中国'
    # read data
    data_topic = pd.read_csv('data_topic.csv')

    try:
        similarity = [model.wv.similarity(prime, theme_class[i]) for i in range(len(theme_class))]
    except KeyError:
        print("******Theme not in the vocab. Input Again*******")

    max_similarity_index = np.argmax(similarity)
    theme = theme_class[max_similarity_index]

    if theme == '艰难':
        theme = '艰难不易'
    if theme == '中国':
        theme = '中国风'

    data = data_topic[data_topic['topic'] == theme]
    data = data.reset_index(drop = True)

    rand_index = random.randrange(0,len(data),1)

    return theme, data.loc[rand_index]['lyric']

if __name__ == '__main__':

    print("Input Topic")
    sys.stdout.write('>')
    sys.stdout.flush()
    prime = sys.stdin.readline()
    prime = prime[:-1]
    theme, sentence = Topic_Generation(prime)
    print("Classified to the theme --- ", theme)
    print("The first sentence:", sentence)