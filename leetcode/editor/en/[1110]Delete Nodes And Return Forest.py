# Given the root of a binary tree, each node in the tree has a distinct value. 
# 
#  After deleting all nodes with a value in to_delete, we are left with a 
# forest (a disjoint union of trees). 
# 
#  Return the roots of the trees in the remaining forest. You may return the 
# result in any order. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,2,4,null,3], to_delete = [3]
# Output: [[1,2,4]]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the given tree is at most 1000. 
#  Each node has a distinct value between 1 and 1000. 
#  to_delete.length <= 1000 
#  to_delete contains distinct values between 1 and 1000. 
#  
# 
#  Related Topics Array Hash Table Tree Depth-First Search Binary Tree 👍 4694 ?
# ? 144


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        to_delete = set(to_delete)
        q = deque()
        ans = [root] if root.val not in to_delete else []
        q.append(root)
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                if node.left.val in to_delete:
                    node.left = None
            if node.right:
                q.append(node.right)
                if node.right.val in to_delete:
                    node.right = None
            if node.val in to_delete:
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)

        return ans

# leetcode submit region end(Prohibit modification and deletion)
