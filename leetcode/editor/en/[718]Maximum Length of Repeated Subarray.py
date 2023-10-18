# Given two integer arrays nums1 and nums2, return the maximum length of a 
# subarray that appears in both arrays. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 100 
#  
# 
#  Related Topics Array Binary Search Dynamic Programming Sliding Window 
# Rolling Hash Hash Function 👍 6535 👎 160


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
