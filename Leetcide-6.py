# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:50:21 2016

@author: ceciliaLee
"""

class Solution:
    
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ## 如果row＝＝0，则下一个s放在当前row的下一行；
        ## 如果row＝＝numRows-1, 则下一个s放在row的上一行（往上走，step＝－1，row＝row＋step）
        ## 依次将s的字符让乳不同的row（每一个row的字符用［］存储）
        ## 最后将numRows个［］串联起来
        if len(s)<=numRows or numRows==1:
            return s
        zigzag=['' for i in range(numRows)]

        row=0
        step=1
        for c in s:
            zigzag[row]+=c
            if row==0:
                step=1
            elif row==numRows-1:
                step=-1           
            row+=step
        return ''.join(zigzag)
        
        
    def __init__(self, s, numRows):  
        self.s=s
        self.numRows=numRows
        self.ans=self.convert(s, numRows)      
        
    def test(self):
        print self.ans
    
s="PAYPALISHIRING"
numRows=3
sol = Solution(s, numRows)
sol.test()