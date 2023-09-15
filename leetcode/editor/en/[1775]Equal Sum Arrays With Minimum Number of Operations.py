# You are given two arrays of integers nums1 and nums2, possibly of different 
# lengths. The values in the arrays are between 1 and 6, inclusive. 
# 
#  In one operation, you can change any integer's value in any of the arrays to 
# any value between 1 and 6, inclusive. 
# 
#  Return the minimum number of operations required to make the sum of values 
# in nums1 equal to the sum of values in nums2. Return -1 if it is not possible to 
# make the sum of the two arrays equal. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
# Output: 3
# Explanation: You can make the sums of nums1 and nums2 equal with 3 operations.
#  All indices are 0-indexed.
# - Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
# - Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
# - Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
# Output: -1
# Explanation: There is no way to decrease the sum of nums1 or to increase the 
# sum of nums2 to make them equal.
#  
# 
#  Example 3: 
# 
#  
# Input: nums1 = [6,6], nums2 = [1]
# Output: 3
# Explanation: You can make the sums of nums1 and nums2 equal with 3 operations.
#  All indices are 0-indexed. 
# - Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
# - Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
# - Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length, nums2.length <= 10⁵ 
#  1 <= nums1[i], nums2[i] <= 6 
#  
# 
#  Related Topics Array Hash Table Greedy Counting 👍 851 👎 37


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 == s2:
            return 0
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1

        arr = [6 - v for v in nums1] + [v - 1 for v in nums2]
        diff = s2 - s1
        for i, v in enumerate(sorted(arr, reverse=True), 1):
            diff -= v
            if diff <= 0:
                return i
        return -1

# leetcode submit region end(Prohibit modification and deletion)
