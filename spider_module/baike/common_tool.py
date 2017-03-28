'''
    通用工具
    1.提取某个标签中的全部文本如<header></header>信息
'''

import re
from urllib import parse

# tag可以是html中的任一标签,先截取一段在使用bs4解析应该会快些
# 使用正则表达式非贪婪匹配提取,也就是说如果有多个相同的标签
# 这个函数只会提取匹配到的第一个标签
# input: tag:str default = "html" (tag = "body","div","a"....)
# return:返回这颗标签的dom树,如果没有找到或者content本身为空,返回NoneType


def get_tag(content, tag="html"):
    if content is not None and content is not "":
        regex_str = r"<"+tag+".*?</"+tag+">"
        # caution: python中的.不匹配换行符\n,所以多行文本不加re.S标志位,它会一行一行的匹配
        match = re.search(re.compile(regex_str, re.S), content)
        if match is not None:
            return match.group()
        else:
            return None
    else:
        return None

# 转换一些进行了url编码的链接,并加上base_url


def format_url(base, url):
    new_url = parse.unquote(url)
    formatted = parse.urljoin(base, new_url)
    return formatted

