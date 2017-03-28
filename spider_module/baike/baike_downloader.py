'''
    @author plyu
    网页下载器:
    input: wanted download url
    output: return the static web page content
    每个下载器管理自己需要下载的url,所需url由urlmanager分发
'''

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
                    rep = requests.get(url, headers=self.headers)
                    rep.raise_for_status()
                    rep.encoding = rep.apparent_encoding
                    html_content = rep.text
                    body = common_tool.get_tag(html_content, "body")
                    if body is not None:
                        self._content_list.append(body)
                except Exception as e:
                    print(e.args)
                    continue

    def add_task_list(self, urls):
        # 当下载器将 task_list中的url全部下载完时才允许添加新的任务url
        if len(self._task_list) == 0:
            for url in urls:
                self._task_list.append(url)

    def get_result_list(self):
        result_list = self._content_list
        self._content_list = []
        return result_list

if __name__ == "__main__":
    target_urls = ["http://aike.baidu.com/ite/python", "http://baike.baidu.com/item/Python"]
    bkspyder = BKDownLoader()
    bkspyder.add_task_list(target_urls)
    bkspyder.download()
    r = bkspyder.get_result_list()
    # print(format(r[0]))