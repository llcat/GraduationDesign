"""
    百科爬虫解析器
    1.提取inner链接,保存在list中
    2.提取内容,因为后续要做高频词汇的提取,所以我这次需要提取更多的内容,不再仅仅提取简介呢
    3.新增需要解析的内容, 词条标签, 历史编辑次数, 词条创建者,最近一次编辑时间(YYYY - MM - DD)

"""
import re
from bs4 import BeautifulSoup
from spider_module.baike.persistence_tool import BKPersistenceTool


class BKParser(object):

    def __init__(self, lemma_content, parser="html.parser"):
        self.lemma_content = lemma_content
        self.soup = BeautifulSoup(lemma_content['body'], parser)

    # 经分析百度百科的词条页面发现,可能是由于百科产品迭代的原因,词条页存在两种url格式
    # 1. href = /item/%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91
    # 2. href = /view/1703056.htm
    # 这可能对我们的去重造成困扰,可能导致词条有两个的url,我们可能会爬了重复的页面,所以后期我们在实际存数据库的时候还是给词条的title建立唯一索引
    def get_inner_link(self):
        result = []
        regex1 = r"/item/.*"
        # regex2 = r"/view/\d+\.htm"
        result1 = self.soup.find_all("a", href=re.compile(regex1))
        # result2 = self.soup.find_all("a", href=re.compile(regex2))
        for res in result1:
            result.append(
                    {
                        "lemma_id": res['href'],
                        "url": res['id']
                    }
            )
        return result  # , result2

    # 取得标题和内容
    def get_content(self):
        # 根据css查找
        title = self.soup.find("dd", class_="lemmaWgt-lemmaTitle-title")
        if title is None:
            title = "err"
        else:
            title = title.h1.string
        paras = self.soup.find_all("div", class_="para")
        para_count = len(paras)
        content = ""
        if para_count > 80*2:
            for i in range(int(para_count/2)):
                text = paras[i].get_text()
                if text is not ""and text is not None:
                    content += text
        else:
            for j in range(para_count):
                text = paras[j].get_text()
                if text is not "" and text is not None:
                    content += text
        return title, content, self.download_url

    # 取得一个词条的人工分类
    def get_lemma_tags(self):
        lemma_tags = self.soup.find_all('span', class_='tag-list')
        for tag in lemma_tags:
            print(tag)


if __name__ == "__main__":
    urls = ["http://baike.baidu.com/item/Python",
            "http://baike.baidu.com/item/%E8%B5%84%E4%BA%A7%E7%AE%A1%E7%90%86%E5%85%AC%E5%8F%B8"]
    import spider_module.baike.baike_downloader as bkd
    import spider_module.baike.common_tool as ctool
    import urllib.parse as p
    bkspyder = bkd.BKDownLoader()
    bkspyder.add_task_list(urls)
    bkspyder.download()
    r = bkspyder.get_result_list()
    # print(r[0]['body'])
    bkparser = BKParser(r[1]['url'], r[1]['body'], "lxml")
    res1 = bkparser.get_inner_link()
    for a in res1[:20]:
        pass
        # print(a)
        # print(type(a['href']))
        # print(p.unquote(a['href']))
        # print(ctool.format_url("http://baike.baidu.com/item/ypl/ss", a))
    t, c, url = bkparser.get_content()
    print(t)
    print(c)
    print(url)
    bkparser.get_lemma_tags()






