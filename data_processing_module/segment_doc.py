"""
    1.应该提取名词作为作为词条的特征值
    2.对于有的词条来说,可能有很多高频词,而有的很少,现阶段我们
      取的范围相对大些,后期在做细化
    3.根据提议,需要修改抓取的内容,增加新的信息

"""

from pymongo import MongoClient as mongoc
from jieba import posseg


class DBUtil(object):
    def __init__(self):
        self.client = mongoc()
        self.db = self.client['spider_module_data']
        self.coll_content = self.db['lemma_contents']
        # self.coll_segmented_doc = self.db['seg_doc']

    def get_contents(self, index=0, quantity=1):
        q_results = self.coll_content.find({}, skip=index, limit=quantity)
        return [content for content in q_results]

    def filter_contents(self, contents, para_size):
        count = 0
        for content in contents:
            if len(content['lemma_paras']) > para_size:
                print(content["lemma_url"])
                print(seg_frequent_words(content['lemma_paras']))
                count += 1
                print(count)

    def update_freq_word(self, filters, add_data):

        try:
            self.coll_content.update_one(filters, add_data)
            return True
        except Exception as e:
            print("in add freq word", e.args)
            return False


def seg_frequent_words(doc, **kargs):
    """
    :param doc: 待提取的文档
    :param kargs:
            top:int - 至少提取前top个高频词,少于top个词则全部提取
            freq:int - 词频大小,如果第top个词频 >> freq,继续向后提取
            allows:[] - default ['n'], ['n','v','adj',......]
    :return: 按照词频排列的list
    """
    top = 8
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
    # 如果提取的高频词的数量大于定义的top个,那么根据词频来判断截取前多少个
    if top < length:
        while s_items[top-1][1] >= freq:
            if top < length:
                top += 1
        return s_items[:top]
    else:
        return s_items


def add_freq_word():
    mongo_util = DBUtil()
    lemma_count = mongo_util.coll_content.count()
    q_r = mongo_util.get_contents(0, lemma_count)
    for content in q_r:
        if "freq_words" not in content.keys():
            doc = content['lemma_paras']
            f_words = seg_frequent_words(doc,)
            condition = {
                            "lemma_id": content['lemma_id']
                        }

            up_data = {
                    "$set": {
                        "freq_words": f_words,
                    }
                }

            mongo_util.update_freq_word(condition, up_data)
        else:
            print("the lemma has freq_words")
    print("seg all document, task done ...")

if __name__ == "__main__":
    db_util = DBUtil()
    q = db_util.get_contents(200, 1)
    # db_util.filter_contents(q, 5000)
    do = q[0]['lemma_paras']
    print(q[0]['lemma_title'], " ", q[0]['lemma_url'])
    l = seg_frequent_words(do,)
    # db_util.coll_segmented_doc.insert_one({'freq_words': l})
    print(l)
    # cursor = db_util.coll_segmented_doc.find_one({})
    # print(cursor['freq_words'])
    # for c in cursor['freq_words']:
    #     print(type(c))
    #     print(c)
    # add_freq_word()