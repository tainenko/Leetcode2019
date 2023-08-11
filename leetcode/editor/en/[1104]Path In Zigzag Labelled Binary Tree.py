# In an infinite binary tree where every node has two children, the nodes are 
# labelled in row order. 
# 
#  In the odd numbered rows (ie., the first, third, fifth,...), the labelling 
# is left to right, while in the even numbered rows (second, fourth, sixth,...), 
# the labelling is right to left. 
# 
#  
# 
#  Given the label of a node in this tree, return the labels in the path from 
# the root of the tree to the node with that label. 
# 
#  
#  Example 1: 
# 
#  
# Input: label = 14
# Output: [1,3,4,14]
#  
# 
#  Example 2: 
# 
#  
# Input: label = 26
# Output: [1,2,6,10,26]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= label <= 10^6 
#  
# 
#  Related Topics Math Tree Binary Tree 👍 1408 👎 298


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        i = x = 1
        while 2 * x <= label:
            x *= 2
            i += 1
        res = [0] * i
        while i:
            res[i - 1] = label
            label = (2 ** (i - 1) + 2 ** i - 1 - label) // 2
            i -= 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
