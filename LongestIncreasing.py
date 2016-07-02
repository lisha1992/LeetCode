# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 13:36:21 2016

@author: ceciliaLee
"""

# scan the array and initialize a new list ans[j] to store，
# use Binary search find the position that nums[i] should be inserted，
# if j>i，ans.append(nums[i]) to keep the original ascending orser of ans
# otherwise, replace
def lengthOfLIS1(nums):
    import bisect
    ans=[]
    for num in nums:
        insertIdx = bisect.bisect_left(ans, num) # copy (insert and return the inserted index)
        if insertIdx==len(ans):
            ans.append(num)
        else:
            ans[insertIdx]=num
    return len(ans)

# ans用来存储最终的升序子序列
# 初始时ans[0]=nums[0]，逐个向后比较nums[x]，用二分法，确定nums[x]在ans中的位置：
#   如果比当前ans的最大值还要大，则加在ans后面
#   如果开始比某个值小了，则把它放在这个值的位置上

def lengthOfLIS2(nums):
    ans=[]
    for num in range(len(nums)):
        low, high=0, len(ans)-1
        
        while low<=high: 
            mid=(low+high)/2
            if ans[mid]<nums[num]: 
                low=mid+1
            else:  
                high=mid-1
        if low>=len(ans):
            ans.append(nums[num])
        else:
            ans[low]=nums[num]
    return len(ans)
            
        
    
        
    
