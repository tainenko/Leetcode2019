# Given two binary search trees root1 and root2, return a list containing all 
# the integers from both trees sorted in ascending order. 
# 
#  
#  Example 1: 
#  
#  
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
#  
# 
#  Example 2: 
#  
#  
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each tree is in the range [0, 5000]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Search Tree Sorting Binary 
# Tree 👍 2882 👎 83


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []

        def dfs(root, l):
            if not root:
                return
            dfs(root.left, l)
            l.append(root.val)
            dfs(root.right, l)

        l1=[]
        l2=[]
        dfs(root1,l1)
        dfs(root2,l2)
        i=j=0
        while i<len(l1) and j<len(l2):
            if l1[i]<l2[j]:
                res.append(l1[i])
                i+=1
            else:
                res.append(l2[j])
                j+=1
        res+=l1[i:]
        res+=l2[j:]
        return res

# leetcode submit region end(Prohibit modification and deletion)
