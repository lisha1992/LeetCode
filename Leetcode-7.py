# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:39:26 2016

@author: SharonLee
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        temp = abs(x)
        while temp>0:
            ans = ans * 10 + temp % 10
            temp /= 10
        if x>=0:
            return ans
        else:
            return ans*(-1)
            
    def __init__(self, x):  
        self.x=x
        self.ans=self.reverse(x)
    
    def test(self):
        print self.ans
            
            
x=123
y=-123
sol1=Solution(x)
sol1.test()  
sol2=Solution(y) 
sol2.test()    

            
            
        