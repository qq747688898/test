import re
import time

'''
先把整个.c文件读入一个大字符串，对其进行第一步预处理
处理/* */，//注释和""包含的字符串常量
'''
def remove_comment_and_string():
    f = open("merge.c")
    all_text = f.read()
    f.close
    Rule = "(\/\*(\s|.)*?\*\/)|(\/\/.*)|(\"(\s|.)*?\")"
    c1 = re.compile(Rule)
    all_text = re.sub(Rule,"",all_text)
    return all_text

'''
将处理了一次的字符串以空格和各个标点为切分符切分成单独单词存入列表
'''
def string_cut(str):
    list1 = re.split(r'\s|\;|\:|\(|\)|\{|\}',str)
    return list1
'''
筛选出列表里的非空、长度在2-8、只含有小写字母的元素，传入一个新的列表
PS：直接对列表操作经常会因为表长改变无法达到预期的效果
'''
def list_space_delete(list):

    list1 = []
    for i in  list:
        if i == ' ':
            continue
        else:
            if i == '':
                continue                              
            else:
                if i.islower() == 0:
                    continue
                else:
                    
                    if len(i) < 2 or len(i) > 8:
                        continue
                    else:
                    
                        list1.append(i)
                '''   
                    else:
                    if len(list[i]) > 8:
                        del list[i]
                '''
                

    return list1
    

'''
整个预处理的主函数
'''
    
def main_pretreat():
    list1 = list_space_delete(string_cut(remove_comment_and_string()))
    return list1



    
    
