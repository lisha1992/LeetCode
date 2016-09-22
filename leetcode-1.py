# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 19:28:18 2016

@author: ceciliaLee
"""

def twoSum(nums, target):
    ## Hash, dictionary
    dic={}
    for index, num in enumerate(nums):
       # print index, num
        key =target-num
        if key in dic:
            return [dic[key], index]
        dic[num]=index
        

nums = [2, 7, 11, 15]
target = 9
ans=twoSum(nums, target)
print ans
