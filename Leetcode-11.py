# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:53:21 2016

@author: SharonLee
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ##  The max volume -> max area of (j-i)*min_height(height[i], height[j])
        left, right, maxA=0,len(height)-1,0  ## Initialize
        while left<right:
            area=min(height[left], height[right])*(right-left)
            maxA=max(area,maxA)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxA
    def __init__(self,height):
        self.height=height
        self.ans=self.maxArea(height)
        
    def test(self):
        print self.ans
        
sol = Solution([1,1])
print 'solution of height=[1,1]'
sol.test()
print 'solution of height=[1,2,3,1,3,1]'
sol = Solution([1,2,3,1,3,1])
sol.test()