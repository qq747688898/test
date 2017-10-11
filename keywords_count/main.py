import time
import re
import Text_Pretreatment as TP
import get_keywords as gk
import KMP


def data_output(list1,list2):
    f = open("output.txt","w")
    j = 0
    for i in list1:
        f.write(i + ':'+str(list2[j]) + '\n')
        j += 1


def main():
    list_count = []
    
    time_TP_start = time.time()
    list_txt = TP.main_pretreat()
    time_TP_end = time.time()
    list_keywords = gk.get_keywords()
    for z in list_keywords:
        list_count.append(int(0))
    time_match_start = time.time()
    
    for i in list_keywords:
        for j in list_txt:
            if j == i:
                list_count[list_keywords.index(i)] +=1
            else:
                continue
    time_match_end = time.time()
    data_output(list_keywords,list_count)
    print('预处理时间为：'+ str(time_TP_end - time_TP_start) + '\n')
    print('匹配的时间为：'+ str(time_match_end - time_match_start) + '\n')
    print('共用时：' + str(time_match_end+time_TP_end-time_match_start-time_TP_start) + '\n')
    return True
    
            
    
