 # 4. Median of Two Sorted Arrays

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1, nums2 = sorted(nums1 + nums2), []
        mid = len(nums1) // 2
        return (nums1[mid] + nums1[~mid]) / 2



# This code aims to find the median (middle value) of two sorted lists of numbers. 
# It merges the two lists, sorts them, and then calculates the median by averaging the middle value and its symmetric counterpart. 
# While it achieves its goal, the approach involves some unnecessary sorting and merging, which could be simplified for efficiency.


