# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 00:54:05 2016

Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    ## start and end represent the start index and end index of the sub-string
    # taverse from left to right, every time end+=1
    # use the dictionary dic to recond the number of strings in the current legitimate substring
    # when a repeat char occurs, which means dict[char]>1: move the start by +1, sic[s[start]]-1, 
    # until dict[char]<1
    
    start, end=0,0
    ans=0
    dic={}
    for c in s:
        end+=1
        dic[c]=dic.get(c, 0)+1
        while dic[c]>1:
            dic[s[start]]-=1
            start+=1
        ans=max(ans, end-start)
    return ans
    
    
    
s1="abcabcbb"
ans1=lengthOfLongestSubstring(s1)
s2="bbbbbb"
ans2=lengthOfLongestSubstring(s2)
s3="pwwkew"
ans3=lengthOfLongestSubstring(s3)
print ans1
print ans2
print ans3