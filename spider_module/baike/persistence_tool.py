"""
    @author: plyu
    百科爬虫持久化工具(使用mongoDB数据库)
    1.保存待爬取url
    2.查找已爬取url
    3.保存词条页的标题和内容
"""
from pymongo import MongoClient as mongoc


class BKPersistenceTool(object):

    def __init__(self,):
        pass

    # 添加一组新的url到数据库中
    def add_new_urls(self, urls):
        pass

    # 判断一个url是否被爬取过
    def is_crawled(self, url):
        pass

    # 取得一个待爬取的任务列表
    # length:制定任务列表长度
    # return:返回任务列表
    def get_task_list(self, length):
        pass

    # content:词条,词条内容,url
    # return:正常添加返回True,否则抛出异常,返回False
    def add_content(self, content):
        pass

