# 重写百科spider,上一个实现不是很稳定而且速度很慢
# 目标:
# 1.能稳定爬取,目的是爬取50W条百度百科词条,并提取相关内容存储到mongoDB数据库中.
# 2.较上次的爬虫实现,加入代理,加入多进程,更改urllib2库为requests库.
# 3.强化下url管理器模块,上一个url的去重实现相对暴力,太low,找一个更好的实现策略.
# 4.后续想到再加


