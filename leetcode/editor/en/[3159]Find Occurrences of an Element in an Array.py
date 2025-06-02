# You are given an integer array nums, an integer array queries, and an integer 
# x. 
# 
#  For each queries[i], you need to find the index of the queries[i]ᵗʰ 
# occurrence of x in the nums array. If there are fewer than queries[i] occurrences of x, 
# the answer should be -1 for that query. 
# 
#  Return an integer array answer containing the answers to all queries. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [1,3,1,7], queries = [1,3,2,4], x = 1 
#  
# 
#  Output: [0,-1,2,-1] 
# 
#  Explanation: 
# 
#  
#  For the 1ˢᵗ query, the first occurrence of 1 is at index 0. 
#  For the 2ⁿᵈ query, there are only two occurrences of 1 in nums, so the 
# answer is -1. 
#  For the 3ʳᵈ query, the second occurrence of 1 is at index 2. 
#  For the 4ᵗʰ query, there are only two occurrences of 1 in nums, so the 
# answer is -1. 
#  
# 
#  Example 2: 
# 
#  
#  Input: nums = [1,2,3], queries = [10], x = 5 
#  
# 
#  Output: [-1] 
# 
#  Explanation: 
# 
#  
#  For the 1ˢᵗ query, 5 doesn't exist in nums, so the answer is -1. 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length, queries.length <= 10⁵ 
#  1 <= queries[i] <= 10⁵ 
#  1 <= nums[i], x <= 10⁴ 
#  
# 
#  Related Topics Array Hash Table 👍 144 👎 19


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

# leetcode submit region end(Prohibit modification and deletion)
