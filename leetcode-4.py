# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 14:20:00 2016

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""
## Idea（binary search, recursive）:
#     求A,B的中位数即求两个list排序后第(m+n)/2 小的数，于是将问题转化为求第k小的数问题，k=(m+n)/2
#     assume that A=[A1,A2,A3,A4,....Am], B[B1,B2,B3,B4,...Bn]
#     compare A[k/2-1] and B[k/2-1]:
#       if A[k/2-1]<B[k/2-1]:
#           第k小的数不可能出现在A[0:k/2-1],可以将A[0:k/2-1]的数ignore，
#           求A[k/2:m]与B[0,k/2-1]的第(k-k/2＋1)小的数
class Solution:
    def get_k_small(self, A, B, k):
        A_len=len(A)
        B_len=len(B)
        if A_len > B_len:
            return self.get_k_small(B, A, k)
        if A_len==0:
            return B[k-1]
        if k==1:
            return min(A[0],B[0])
        A_pt=min(k/2, A_len)
        B_pt=k-A_pt
        if A[A_pt-1]<=B[B_pt-1]:
            return self.get_k_small(A[A_pt:], B, B_pt)
        else:
            return self.get_k_small(A, B[B_pt:], A_pt)
            
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1=len(nums1)
        len2=len(nums2)
        k=(len1+len2)/2
        if (len1+len2)%2==1:
            return self.get_k_small(nums1,nums2,k+1)
        else:
            return 0.5*( self.get_k_small(nums1,nums2, k) + self.get_k_small(nums1,nums2, k+1 )) 
        
    def __init__(self,nums1,nums2):
        self.nums1=nums1
        self.nums2=nums2
        self.ans=self.findMedianSortedArrays(nums1, nums2)
        
    def test(self):
        print self.ans
        
sol = Solution([2,3,4],[1])
sol.test()
