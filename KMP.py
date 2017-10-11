'''
一个KMP算法的Python语句实现。由于我把所有文本都切分成了单词而不是字符串，所以
最后还是采用了最原始的匹配方式
'''
def partial_table(p):
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1,len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i+1] for j in range (1,i+1)}
        ret.append(len((prefix&postfix or {''}).pop()))
    return ret    

def KMP_match(str1,str2):
    m = len(str1)
    n = len(str2)
    cur = 0
    table = partial_table(str2)
    while cur <= m-n:
        for i in range(n):
            if str1[i+cur] != str2[i]:
                cur += max(i - table[i-1])
                break
        else:
            return True
    return False
