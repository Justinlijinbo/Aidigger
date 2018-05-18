# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 20:53:09 2018

@author: JINBOLI
"""
test1 = "adcbf"
dict1 = {'a': ['B', 'C'], 'b': ['X'], 'c':['Y','Z']}

#def generate(text : str, map : Dict[str, str]):
#
#    pass

def generate(text : str , dict : [str, str]):
    '''result 为每个字母 取字典相对应的结果值 返回一个list'''
    result = []
    for word in text:
        if word in dict.keys():
            res = dict[word]
            result.append(res)
        else :
            result.append([word])
        
    return result

res1 = generate(test1,dict1)


def combine_two_list(list1,list2):
    ''' 每 2个generate生成的list 生成结果 '''
    res = []
    for i in list1:
        for j in list2:
            res.append(i+j)
    return res


result = res1[0]
for i in res1:
    if i != res1[0]:
        result = combine_two_list(result,i)
        
print(result)        
