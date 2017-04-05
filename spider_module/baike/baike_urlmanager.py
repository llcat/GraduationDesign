"""
    bai_ke url管理器:
    1.分发 task url到下载器
    2.存储待爬url到db
"""

from spider_module.baike import common_tool as ctool
from spider_module.baike import persistence_tool as ptool


class BKUrlManager(object):

    def __init__(self):
        self.p_tool = ptool.BKPersistenceTool()
        self.task_list = []

    def save_urls(self, base, urls):
        f_urls = ctool.get_formatted_urls(base, urls)
        self.p_tool.add_new_urls(f_urls)

    def dispatch_task(self, downloaders):
        downloader_num = len(downloaders)
        if len(self.task_list) <= 0:
            self.supply_task_list()
        task_count = len(self.task_list)
        per_tasks = task_count/downloader_num
        for downloader in downloaders:
            downloader.add_task_list(self.task_list)

    def supply_task_list(self):
        pass