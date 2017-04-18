"""
    @author plyu
    网页下载器:
    input: wanted download url
    output: return the static web page content
    每个下载器管理自己需要下载的url,所需url由urlmanager分发
"""
import os
import requests
import random
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
            for task in self._task_list:
                try:
                    lemma_content = {}
                    rep = requests.get(task['url'], headers=self.headers)
                    rep.raise_for_status()
                    rep.encoding = rep.apparent_encoding
                    html_content = rep.text
                    lemma_content['lemma_id'] = task['lemma_id']
                    lemma_content['url'] = task['url']
                    lemma_content['body'] = common_tool.get_tag(html_content, "body")
                    if lemma_content['body'] is None:
                        continue

                    new_lemmaid_enc = common_tool.get_newlemmaid_enc(html_content)
                    lemma_content['lemmaid_enc'] = new_lemmaid_enc
                    rep1 = self.get_share_count(task['lemma_id'])
                    if rep1 is not False:
                        lemma_content['like_count'] = rep1['likeCount']
                        lemma_content['share_count'] = rep1['shareCount']
                    else:
                        lemma_content['like_count'] = "null"
                        lemma_content['share_count'] = "null"

                    if new_lemmaid_enc == "null":
                        lemma_content['history_view_count'] = "null"
                    else:
                        print(new_lemmaid_enc, type(new_lemmaid_enc))
                        rep2 = self.get_view_count(new_lemmaid_enc)
                        print(rep2)
                        if rep2 is not False:
                            lemma_content['history_view_count'] = rep2['pv']
                        else:
                            lemma_content['history_view_count'] = "null"
                    if lemma_content['body'] is not None:
                        self._content_list.append(lemma_content)
                    else:
                        print("the %s is missing,check miss.txt" % task['url'])
                        with open("miss.txt", "a") as f:
                            f.write(task['url']+"-"+task['lemma_id']+"\n")

                except Exception as e:
                    print(e.args)
                    continue
            self.clear_task_list()

    def add_task_list(self, tasks):
        # 当下载器将 task_list中的url全部下载完时才允许添加新的任务url
        if len(self._task_list) == 0:
            for task in tasks:
                self._task_list.append(task)
        else:
            print("task list still has url, nums:%d" % (len(self._task_list)))

    def get_result_list(self):
        result_list = self._content_list
        self._content_list = []
        return result_list

    def clear_task_list(self):
        self._task_list = []
        print("downloader-%d clear task list" % (os.getpid()))

    def download_raw(self, url):
        """
        :param url:
        :return: 返回requests库请求的全部内容
        """
        try:
            rep = requests.get(url, headers=self.headers,)
            rep.raise_for_status()
            rep.encoding = rep.apparent_encoding
            raw_content = rep.text
            return raw_content
        except Exception as e:
            print("in download raw:", e.args)

    def get_share_count(self, lemma_id):
        """
        根据词条id返回该词条的share_count和like_count
        :param lemma_id:
        :return:
        """
        api = "http://baike.baidu.com/api/wikiui/sharecounter"
        params = {"lemmaId": lemma_id,
                  "method": "get"}
        result = self.down_json(api, params)
        if result is False:
            print("get share count failed....")

        return result

    def get_view_count(self, new_lemmaid_enc):
        """
        取得词条的历史浏览次数
        :param new_lemmaid_enc:
        :return:
        """
        api = "http://baike.baidu.com/api/lemmapv"
        params = {"id": new_lemmaid_enc,
                  "r": random.random()}
        result = self.down_json(api, params)
        if result is False:
            print("get view count failed....")

        return result

    def down_json(self, api, params):
        try:
            rep = requests.get(api, params=params,headers=self.headers)
            rep.raise_for_status()
            rep.encoding = rep.apparent_encoding
            json_data = rep.json()
            return json_data
        except Exception as e:
            print("in down_json:", e.args)
            return False


if __name__ == "__main__":
    target_urls = [
        {
            "lemma_id": 85979,                                                 "url": "http://baike.baidu.com/item/Java"
        },
    ]
    bkspyder = BKDownLoader()
    bkspyder.add_task_list(target_urls)
    bkspyder.download()
    # r = bkspyder.get_result_list()
    # print(r)
    k = bkspyder.get_share_count(85979)
    print(k)
    id_enc = "eca9aca485477e4ed52788f4"
    j = bkspyder.get_view_count(id_enc)
    print(j)
