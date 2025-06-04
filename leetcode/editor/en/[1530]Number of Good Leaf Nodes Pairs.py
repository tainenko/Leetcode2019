# You are given the root of a binary tree and an integer distance. A pair of 
# two different leaf nodes of a binary tree is said to be good if the length of the 
# shortest path between them is less than or equal to distance. 
# 
#  Return the number of good leaf node pairs in the tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the 
# shortest path between them is 3. This is the only good pair.
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The 
# pair [4,6] is not good because the length of ther shortest path between them is 4.
# 
#  
# 
#  Example 3: 
# 
#  
# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# Explanation: The only good pair is [2,5].
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 2¹⁰]. 
#  1 <= Node.val <= 100 
#  1 <= distance <= 10 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 2455 👎 108


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        def dfs(root, cnt, i):
            if root is None or i >= distance:
                return
            if root.left is None and root.right is None:
                cnt[i] += 1
                return
            dfs(root.left, cnt, i + 1)
            dfs(root.right, cnt, i + 1)

        if not root:
            return 0
        ans = self.countPairs(root.left, distance) + self.countPairs(root.right, distance)
        cnt1 = Counter()
        cnt2 = Counter()
        dfs(root.left, cnt1, 1)
        dfs(root.right, cnt2, 1)
        for k1, v1 in cnt1.items():
            for k2, v2 in cnt2.items():
                if k1 + k2 <= distance:
                    ans += v1 * v2
        return ans
# leetcode submit region end(Prohibit modification and deletion)
