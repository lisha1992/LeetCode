# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 18:41:38 2016

@author: sharonLee
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ## Partition the orihinal integer one by one, 
        ## Judge whether the first number is equal to the last one
        
        if x<0:  ## All negative integers are not palindrome
            return False
        
        num=1
        while x/num>=10:
            num=num*10
        
        while num>1:
            right=x%10
            left=x/num
            if left!=right:
                return False

            x=(x%num)/10
            num=num/100
        return True
            


        
    def __init__(self,x):
        self.x=x
        self.ans=self.isPalindrome(x)
        
    def test(self):
        print self.ans
        
        
sol = Solution(1000021)
sol.test()