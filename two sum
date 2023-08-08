 # 1. Two Sum 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Language in Python3


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=0
        for i in range(len(nums)):
            p = target-nums[i]
            if p in nums:
                a=nums.index(p)
                if a==i:
                    continue
                break
        return i,a


