# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5

@author: SharonLee
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## 相同数字相连（<=3），相加得到Int
        ## if s[i]>s[i+1]: 相加得到Int
        ## if s[i]<s[i+1]: Int=s[i+1]-s[i]
        # 如果发现前一个字母比当前字母小，就减去前一个字母，
        # 因为错误的把它加入了结果，且在加上当前字母时还要减去前一个字母的值。
    
        rom2int={"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        
        ans=rom2int[s[0]]
       
        for i in range(1,len(s)):
            if rom2int[s[i]]<=rom2int[s[i-1]]:
                ans+=rom2int[s[i]]
            else:
                ans-=rom2int[s[i-1]]
                ans+=rom2int[s[i]]-rom2int[s[i-1]]
        return ans
                
        
if __name__ == "__main__":
    assert Solution().romanToInt("DCXXI")==621
    assert Solution().romanToInt("MCMXCVI") == 1996