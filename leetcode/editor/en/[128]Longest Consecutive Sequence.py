# Given an unsorted array of integers nums, return the length of the longest con
# secutive elements sequence. 
# 
#  You must write an algorithm that runs in O(n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Theref
# ore its length is 4.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 105 
#  -109 <= nums[i] <= 109 
#  
#  Related Topics Array Hash Table Union Find 
#  👍 6224 👎 289


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = {num: True for num in nums}
        length = 0
        for num in nums:
            if not visited[num]:
                continue
            visited[num] = False
            left = num - 1
            right = num + 1
            while visited.get(left):
                visited[left] = False
                left -= 1
            while visited.get(right):
                visited[right] = False
                right += 1
            length = max(length, right - left - 1)
        return length

    # leetcode submit region end(Prohibit modification and deletion)
