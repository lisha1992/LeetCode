
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
        ## Trun the original integer around (rev)
        ## See whether the reversed integer is equal to the original one
        if x<0:  ## All negative integers are not palindrome
            return False
        temp=x
        rev=0
        while x>0:
            rev=rev*10+x%10
            x=x/10
        if temp==rev:
            return True
        else:
            return False
        
    def __init__(self,x):
        self.x=x
        self.ans=self.isPalindrome(x)
        
    def test(self):
        print self.ans
        
        
sol = Solution(-2147483648)
sol.test()