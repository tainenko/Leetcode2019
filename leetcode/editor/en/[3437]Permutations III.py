# Given an integer n, an alternating permutation is a permutation of the first 
# n positive integers such that no two adjacent elements are both odd or both even.
#  
# 
#  Return all such alternating permutations sorted in lexicographical order. 
# 
#  
#  Example 1: 
# 
#  
#  Input: n = 4 
#  
# 
#  Output: [[1,2,3,4],[1,4,3,2],[2,1,4,3],[2,3,4,1],[3,2,1,4],[3,4,1,2],[4,1,2,3
# ],[4,3,2,1]] 
# 
#  Example 2: 
# 
#  
#  Input: n = 2 
#  
# 
#  Output: [[1,2],[2,1]] 
# 
#  Example 3: 
# 
#  
#  Input: n = 3 
#  
# 
#  Output: [[1,2,3],[3,2,1]] 
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10 
#  
# 
#  Related Topics Array Backtracking 👍 10 👎 1


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, n: int) -> List[List[int]]:
        
# leetcode submit region end(Prohibit modification and deletion)
