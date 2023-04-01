# You are given a 0-indexed integer array nums. 
# 
#  Swaps of adjacent elements are able to be performed on nums. 
# 
#  A valid array meets the following conditions: 
# 
#  
#  The largest element (any of the largest elements if there are multiple) is 
# at the rightmost position in the array. 
#  The smallest element (any of the smallest elements if there are multiple) is 
# at the leftmost position in the array. 
#  
# 
#  Return the minimum swaps required to make nums a valid array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,4,5,5,3,1]
# Output: 6
# Explanation: Perform the following swaps:
# - Swap 1: Swap the 3ʳᵈ and 4ᵗʰ elements, nums is then [3,4,5,3,5,1].
# - Swap 2: Swap the 4ᵗʰ and 5ᵗʰ elements, nums is then [3,4,5,3,1,5].
# - Swap 3: Swap the 3ʳᵈ and 4ᵗʰ elements, nums is then [3,4,5,1,3,5].
# - Swap 4: Swap the 2ⁿᵈ and 3ʳᵈ elements, nums is then [3,4,1,5,3,5].
# - Swap 5: Swap the 1ˢᵗ and 2ⁿᵈ elements, nums is then [3,1,4,5,3,5].
# - Swap 6: Swap the 0ᵗʰ and 1ˢᵗ elements, nums is then [1,3,4,5,3,5].
# It can be shown that 6 swaps is the minimum swaps required to make a valid 
# array.
#  
# 
# Example 2:
# 
#  
# Input: nums = [9]
# Output: 0
# Explanation: The array is already valid, so we return 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics Array Greedy 👍 89 👎 17


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        h_idx = n - 1
        highest = max(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] == highest:
                h_idx = i
                break
        l_idx = nums.index(min(nums))
        if l_idx > h_idx:
            return l_idx + n - h_idx - 2
        return l_idx + n - h_idx - 1

# leetcode submit region end(Prohibit modification and deletion)
