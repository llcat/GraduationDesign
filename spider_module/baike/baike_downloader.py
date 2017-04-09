"""
    @author plyu
    网页下载器:
    input: wanted download url
    output: return the static web page content
    每个下载器管理自己需要下载的url,所需url由urlmanager分发
"""
import os
import requests
from spider_module.baike import common_tool


class BKDownLoader(object):

    def __init__(self):
        self._task_list = []
        self._content_list = []
        self.headers = {
            "Host": "baike.baidu.com",
            "User-Agent": "Mozilla/5.0"
        }

    def download(self):
        if len(self._task_list) > 0:
            for url in self._task_list:
                try:
                    content = {}
                    rep = requests.get(url, headers=self.headers)
                    rep.raise_for_status()
                    rep.encoding = rep.apparent_encoding
                    html_content = rep.text
                    content['body'] = common_tool.get_tag(html_content, "body")
                    content['url'] = url
                    if content['body'] is not None:
                        self._content_list.append(content)
                    else:
                        print("the %s is missing,check miss.txt" % url)
                        with open("miss.txt", "a") as f:
                            f.write(url+"\n")

                except Exception as e:
                    print(e.args)
                    continue
            self.clear_task_list()

    def add_task_list(self, urls):
        # 当下载器将 task_list中的url全部下载完时才允许添加新的任务url
        if len(self._task_list) == 0:
            for url in urls:
                self._task_list.append(url)
        else:
            print("task list still has url, nums:%d" % (len(self._task_list)))

    def get_result_list(self):
        result_list = self._content_list
        self._content_list = []
        return result_list

    def clear_task_list(self):
        self._task_list = []
        print("downloader-%d clear task list" % (os.getpid()))

if __name__ == "__main__":
    target_urls = ["http://aike.baidu.com/ite/python", "http://baike.baidu.com/item/Python"]
    bkspyder = BKDownLoader()
    bkspyder.add_task_list(target_urls)
    bkspyder.download()
    r = bkspyder.get_result_list()
    print(r[0]['body'])