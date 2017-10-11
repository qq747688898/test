import re

'''
通过关键字文件将关键字读取，并且分片存入一个列表
'''
def get_keywords():
    f = open("keywords.txt")
    l = f.read()
    list_keywords=re.split(r'\s',l)
    return list_keywords
