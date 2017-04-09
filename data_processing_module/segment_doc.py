"""
    1.应该提取名词作为作为词条的特征值
    2.对于
"""

from pymongo import MongoClient as mongoc
from jieba import posseg


class DBUtil(object):
    def __init__(self):
        self.client = mongoc()
        self.db = self.client['spider_module_data']
        self.coll_content = self.db['content']
        self.coll_segmented_doc = self.db['seg_doc']

    def get_contents(self, index=0, quantity=1):
        q_results = self.coll_content.find({}, skip=index, limit=quantity)
        return [content for content in q_results]

    def add_freq_words(self, data):
        """
        :param data:
         data = {
                    'title': title
                    'words':{
                                word: count,
                                ...
                            }
                }
        :return:
        """
        pass


def seg_frequent_words(doc, **kargs):
    """
    :param doc: 待提取的文档
    :param kargs:
            top:int - 至少提取前top个高频词,少于top个词则全部提取
            freq:int - 词频大小,如果第top个词频 >> freq,继续向后提取
            allows:[] - default ['n'], ['n','v','adj',......]
    :return: 按照词频排列的list
    """
    top =8
    freq = 10
    allows = ['n']
    for key in kargs:
        if 'top' == key:
            top = kargs[key]
        elif 'freq' == key:
            freq = kargs[key]
        elif 'allows' == key:
            allows = kargs[key]

    segmented = posseg.cut(doc)
    data = {}
    for w, f in segmented:
        if f in allows:
            if w in data.keys():
                data[w] += 1
            else:
                data[w] = 1

    s_items = sorted(data.items(), key=lambda da: da[1], reverse=True)
    length = len(s_items)
    if top < length:
        while s_items[top-1][1] >= freq:
            if top < length:
                top += 1
        return s_items[:top]
    else:
        return s_items


db_util = DBUtil()
q = db_util.get_contents(6)
do = q[0]['content']
print(q[0]['title'])
l = seg_frequent_words(do,)
print(l)