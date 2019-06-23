'''
[15] 3Sum

https://leetcode.com/problems/3sum/description/

* algorithms
* Medium (24.13%)
* Source Code:       15.3sum.py
* Total Accepted:    569.5K
* Total Submissions: 2.4M
* Testcase Example:  '[-1,0,1,2,-1,-4]'

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:


Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums=sorted(nums)
        found=set()
        for idx in range(len(nums)):
            if nums[idx] in found:
                continue
            found.add(nums[idx])
            tmp=self.twoSum(nums[idx+1:],-nums[idx])
            if tmp and tmp not in res:
                res+=tmp
        return res

    def twoSum(self,nums,target):
        tmp={}
        res=[]
        for idx,num in enumerate(nums):
            if num not in tmp:
                tmp[target-num]=idx
            else:
                if [-target,nums[tmp[num]],num] not in res:
                    res.append([-target,nums[tmp[num]],num])
        return res
