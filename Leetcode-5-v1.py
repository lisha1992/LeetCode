# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:41:38 2016

@author: ceciliaLee
"""

class Solution():
     # @param {string} s input string
     # @return {string} the longest palindromic substring

     ## Method1: Brute -force
    ##  穷举所有的可能substr， 判断是否为palindrome， 
    ## 使用variable longest 纪录 the longest palindrome length,
    ## Return the longest substr

    def longestPalindrome(self, s):
        if len(s)==0:
            return ''
        leng=len(s)
        longest, left, right=0,0,0  ## left, right denote the starting and end indeces of the substr respectively
        for i in xrange(leng):
            for j in range(i+1, leng+1):
                substr=s[i:j]
                if self.isPalindrome(substr) and len(substr)> longest:
                    longest=len(substr)
                    left, right=i,j
        return s[left:right] ## loghest palindrome
    
    def isPalindrome(self, s):
        if len(s)==0:
            return False
        return s==s[::-1]  ## Compare s reversely
        
    def __init__(self,s):
        self.s=s
        self.ans=self.longestPalindrome(s)
        
    def test_brute_force(self):
        print self.ans
        
        
sol = Solution('abaabacc')
sol.test_brute_force()