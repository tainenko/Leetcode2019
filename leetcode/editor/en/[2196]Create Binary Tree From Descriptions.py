# You are given a 2D integer array descriptions where descriptions[i] = [
# parenti, childi, isLefti] indicates that parenti is the parent of childi in a binary 
# tree of unique values. Furthermore, 
# 
#  
#  If isLefti == 1, then childi is the left child of parenti. 
#  If isLefti == 0, then childi is the right child of parenti. 
#  
# 
#  Construct the binary tree described by descriptions and return its root. 
# 
#  The test cases will be generated such that the binary tree is valid. 
# 
#  
#  Example 1: 
#  
#  
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
# Explanation: The root node is the node with value 50 since it has no parent.
# The resulting binary tree is shown in the diagram.
#  
# 
#  Example 2: 
#  
#  
# Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
# Output: [1,2,null,null,3,4]
# Explanation: The root node is the node with value 1 since it has no parent.
# The resulting binary tree is shown in the diagram.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= descriptions.length <= 10⁴ 
#  descriptions[i].length == 3 
#  1 <= parenti, childi <= 10⁵ 
#  0 <= isLefti <= 1 
#  The binary tree described by descriptions is valid. 
#  
# 
#  Related Topics Array Hash Table Tree Depth-First Search Breadth-First Search 
# Binary Tree 👍 847 👎 17


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = dict()
        parents = set()
        children = set()
        for p_val, c_val, is_left in descriptions:
            parent = self.get_node(nodes,p_val)
            child = self.get_node(nodes, c_val)
            parents.add(parent)
            children.add(child)
            if is_left:
                parent.left=child
            else:
                parent.right=child
        return list(parents.difference(children))[0]

    def get_node(self, nodes:dict, val:int)->TreeNode:
        if val not in nodes:
            node = TreeNode(val)
            nodes[val]=node
        else:
            node=nodes[val]
        return node

# leetcode submit region end(Prohibit modification and deletion)
