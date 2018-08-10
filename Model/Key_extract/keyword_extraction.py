#encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")
import jieba.analyse
from optparse import OptionParser
import csv

print('='*40)
print('3. 关键词提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)

def load_and_cut_data(filepath):
    '''
    加载数据并分词
    :param filepath: 路径
    :return: data: 分词后的数据
    '''
    # filepath指定了需要读取的文件的路径，'r'表示以只读方式打开，'encoding'指明了文件的编码方式
    with open(filepath, 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        data = []  # 创建一个列表
        for line in reader:
            data.append(line[0])
    return data

if __name__ == '__main__':

    USAGE = "usage: python keyword_extraction.py [file name] [save name] -n [sentence n] -k [top k] -w [with weight=1 or 0]"

    parser = OptionParser(USAGE)
    parser.add_option("-n", dest="SentenceN")
    parser.add_option("-k", dest="topK")
    parser.add_option("-w", dest="withWeight")
    opt, args = parser.parse_args()

    if len(args) < 1:
        print(USAGE)
        sys.exit(1)

    file_name = args[0]
    save_name = args[1]

    if opt.SentenceN is None:
        SentenceN = 2
    else:
        SentenceN = int(opt.SentenceN)

    if opt.topK is None:
        topK = 4
    else:
        topK = int(opt.topK)

    if opt.withWeight is None:
        withWeight = False
    else:
        if int(opt.withWeight) is 1:
            withWeight = True
        else:
            withWeight = False

    print("filename", file_name)
    print("SentenceN", SentenceN)
    print("topK", topK)
    print("withWeight", withWeight)

    # Params
    # Load Data
    data = load_and_cut_data(filepath=file_name)
    extract_len = len(data)
    # Tags Set
    tfidf_tags_set = []
    # allowPOS https://www.cnblogs.com/i80386/p/3403644.html
    # nr-人名 ns-地名 nt-机构团体 n-名词 vn-动名词 v-动词 vd-副动词 an-名形词 i-成语 tg-时语素
    allowPOS = ('nr', 'ns', 'n','nt', 'v', 'vn', 'an', 'tg')

    #------------------------------------------------

    for i in range(0, (extract_len-SentenceN), SentenceN):
        s = ''
        for j in range(i, i + SentenceN):
            s += data[j]
        tfidf_tags = jieba.analyse.extract_tags(s, topK=topK, withWeight=withWeight, allowPOS=allowPOS)
        if tfidf_tags:
            if withWeight:
                data[j] += (',' + tfidf_tags[0][0])
            else:
                data[j] += (',' + tfidf_tags[0])

    fo = open(save_name,'w')
    for i in range(0,extract_len):
        fo.write(data[i]+'\n')
    fo.close()



