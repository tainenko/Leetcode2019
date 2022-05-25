# Given an array nums, return true if the array was originally sorted in non-
# decreasing order, then rotated some number of positions (including zero).
# Otherwise, return false.
#
#  There may be duplicates in the original array.
#
#  Note: An array A rotated by x positions results in an array B of the same
# length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
#
#
#  Example 1:
#
#
# Input: nums = [3,4,5,1,2]
# Output: true
# Explanation: [1,2,3,4,5] is the original sorted array.
# You can rotate the array by x = 3 positions to begin on the the element of
# value 3: [3,4,5,1,2].
#
#
#  Example 2:
#
#
# Input: nums = [2,1,3,4]
# Output: false
# Explanation: There is no sorted array once rotated that can make nums.
#
#
#  Example 3:
#
#
# Input: nums = [1,2,3]
# Output: true
# Explanation: [1,2,3] is the original sorted array.
# You can rotate the array by x = 0 positions (i.e. no rotation) to make nums.
#
#
#
#  Constraints:
#
#
#  1 <= nums.length <= 100
#  1 <= nums[i] <= 100
#
#  Related Topics Array 👍 592 👎 50


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        r = -1
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                r = i
        if count == 0:
            return True
        if count > 1:
            return False
        return nums[r] <= nums[0] and nums[r - 1] >= nums[-1]

# leetcode submit region end(Prohibit modification and deletion)
