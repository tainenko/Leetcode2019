# An array nums of length n is beautiful if: 
# 
#  
#  nums is a permutation of the integers in the range [1, n]. 
#  For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[
# k] == nums[i] + nums[j]. 
#  
# 
#  Given the integer n, return any beautiful array nums of length n. There will 
# be at least one valid answer for the given n. 
# 
#  
#  Example 1: 
#  Input: n = 4
# Output: [2,1,4,3]
#  
#  Example 2: 
#  Input: n = 5
# Output: [3,1,2,5,4]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1000 
#  
# 
#  Related Topics Array Math Divide and Conquer 👍 1111 👎 1555


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
# leetcode submit region end(Prohibit modification and deletion)
