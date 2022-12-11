# Given an array of unique integers preorder, return true if it is the correct 
# preorder traversal sequence of a binary search tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: preorder = [5,2,1,3,6]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: preorder = [5,2,6,1,3]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= preorder.length <= 10⁴ 
#  1 <= preorder[i] <= 10⁴ 
#  All the elements of preorder are unique. 
#  
# 
#  
#  Follow up: Could you do it using only constant space complexity? 
# 
#  Related Topics Stack Tree Binary Search Tree Recursion Monotonic Stack 
# Binary Tree 👍 1032 👎 76


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        res = []
        stack = [preorder[0]]
        for v in preorder[1:]:
            if v < stack[-1]:
                stack.append(v)
                continue
            while stack:
                if v < stack[-1]:
                    stack.append(v)
                    break
                res.append(stack.pop())
            if not stack:
                stack.append(v)
        while stack:
            res.append(stack.pop())
        return res == sorted(res)

# leetcode submit region end(Prohibit modification and deletion)
