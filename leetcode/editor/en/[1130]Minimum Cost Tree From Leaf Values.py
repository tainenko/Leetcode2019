# Given an array arr of positive integers, consider all binary trees such that: 
# 
# 
#  
#  Each node has either 0 or 2 children; 
#  The values of arr correspond to the values of each leaf in an in-order 
# traversal of the tree. 
#  The value of each non-leaf node is equal to the product of the largest leaf 
# value in its left and right subtree, respectively. 
#  
# 
#  Among all possible binary trees considered, return the smallest possible sum 
# of the values of each non-leaf node. It is guaranteed this sum fits into a 32-
# bit integer. 
# 
#  A node is a leaf if and only if it has zero children. 
# 
#  
#  Example 1: 
#  
#  
# Input: arr = [6,2,4]
# Output: 32
# Explanation: There are two possible trees shown.
# The first has a non-leaf node sum 36, and the second has non-leaf node sum 32.
# 
#  
# 
#  Example 2: 
#  
#  
# Input: arr = [4,11]
# Output: 44
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= arr.length <= 40 
#  1 <= arr[i] <= 15 
#  It is guaranteed that the answer fits into a 32-bit signed integer (i.e., it 
# is less than 2³¹). 
#  
# 
#  Related Topics Array Dynamic Programming Stack Greedy Monotonic Stack 👍 4087
#  👎 262


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def dfs(i, j):
            if i == j:
                return 0, arr[i]
            total = inf
            mx = 0
            for k in range(i, j):
                s1, mx1 = dfs(i, k)
                s2, mx2 = dfs(k + 1, j)
                t = s1 + s2 + mx1 * mx2
                if total > t:
                    total = t
                    mx = max(mx1, mx2)
            return total, mx

        return dfs(0, len(arr) - 1)[0]

# leetcode submit region end(Prohibit modification and deletion)
