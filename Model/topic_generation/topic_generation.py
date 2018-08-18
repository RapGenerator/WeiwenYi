import pandas as pd
import sys
import random

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

def Topic_Generation():

    data_topic = pd.read_csv('data_topic.csv')

    print("Topic:", dict_topic.values())
    sys.stdout.write('>')
    sys.stdout.flush()

    prime = sys.stdin.readline()
    prime = prime[:-1]

    if prime not in dict_topic.values():
        raise ValueError('Topic Error')

    data = data_topic[data_topic['topic'] == prime]
    data = data.reset_index(drop = True)

    rand_index = random.randrange(0,len(data),1)

    return data.loc[rand_index]['lyric']

if __name__ == '__main__':
    sentence = Topic_Generation()
    print(sentence)