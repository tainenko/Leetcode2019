#
# @lc app=leetcode id=46 lang=python
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (56.36%)
# Total Accepted:    415.7K
# Total Submissions: 733.4K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def getpermute(nums,arr):
            if not nums or len(nums)==1:
                res.append(arr+nums)
            else:
                for i in range(len(nums)):
                    nums[0],nums[i]=nums[i],nums[0]
                    getpermute(nums[1:],arr+[nums[0]])
                    nums[0], nums[i] = nums[i], nums[0]
        getpermute(nums,[])
        return res

        
