# Given the root of a binary tree, the value of a target node target, and an 
# integer k, return an array of the values of all nodes that have a distance k from 
# the target node. 
# 
#  You can return the answer in any order. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
# Output: [7,4,1]
# Explanation: The nodes that are a distance 2 from the target node (with value 
# 5) have values 7, 4, and 1.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1], target = 1, k = 3
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 500]. 
#  0 <= Node.val <= 500 
#  All the values Node.val are unique. 
#  target is the value of one of the nodes in the tree. 
#  0 <= k <= 1000 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 82
# 56 👎 166


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict, deque


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def dfs(parent: TreeNode, child: TreeNode):
            if not child:
                return
            if parent and child:
                graph[parent.val].append(child.val)
                graph[child.val].append(parent.val)
            dfs(child, child.left)
            dfs(child, child.right)

        dfs(None, root)

        res = deque()
        res.append(target.val)
        visited = set()
        while k:
            for _ in range(len(res)):
                val = res.popleft()
                visited.add(val)
                for n in graph[val]:
                    if n in visited:
                        continue
                    res.append(n)

            k -= 1
        return list(res)

# leetcode submit region end(Prohibit modification and deletion)
