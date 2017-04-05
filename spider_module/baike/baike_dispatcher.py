"""
    @author: pl_yu
    百科爬虫调度器
    调用其他模块,处理全部的业务逻辑
    整理下思路:
    1.结束条件是完成需要爬取的url条数,在start()中给定
    2.主进程和3个downloader间需要通信
      如下载任务完成需要通知url manager进程分派新的url,
      下载完成后的url和内容应该是存放在共享的list的中,3个downloader争用情况下应该加锁

"""

from spider_module.baike.baike_downloader import BKDownLoader
from spider_module.baike.baike_parser import BKParser
from spider_module.baike.persistence_tool import BKPersistenceTool
from spider_module.baike.baike_urlmanager import BKUrlManager
from spider_module.baike.common_tool import *
from multiprocessing import Manager, Process, Queue, Lock


class BKDispatcher(object):

    def __init__(self):
        self.completed_list = Manager().list()
        self.p_tool = BKPersistenceTool()

    def parser(self, d_url, content):
        parser = BKParser(d_url, content, "lxml")
        title, content, url = parser.get_content()
        data = {
            "title": title,
            "url": url,
            "content": content
        }
        self.p_tool.add_content(data)
        urls = parser.get_inner_link()
        formatted = get_formatted_urls(urls)
        self.p_tool.add_new_urls(formatted)

    # url生产者进程
    @staticmethod
    def url_manager(message_que):
        pass

    # url消费者进程(3个),与生产者间使用Queue通信,与主进程共享变量completed_list
    @staticmethod
    def downloader():
        pass

    # 开始任务
    def start(self, task_num):
        while task_num > 0:
            # 进程间通信队列
            d_queues = [{"send_q": Queue(), "receive_q": Queue()}]*3
            # url manager进程
            process_manager = Process(target=self.url_manager, args=(d_queues,))
            process_manager.start()
            # downloader进程
            for d_que in d_queues:
                Process(target=self.downloader, args=(d_que,)).start()

            if len(self.completed_list) > 0:
                content = self.completed_list.pop()
                task_num -= 1
                self.parser(content['url'], content['body'])


