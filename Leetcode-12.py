# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5

@author: SharonLee
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ## The corresponding elements are as follows
        integer=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman=['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        ans=''
        for i in range(len(integer)):
            while num>=integer[i]:
                ans+=roman[i]
                num-=integer[i]
        return ans
        
if __name__ == "__main__":
    assert Solution().intToRoman(3188)=="MMMCLXXXVIII"
    assert Solution().intToRoman(2) == 'II'