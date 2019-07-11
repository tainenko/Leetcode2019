'''
[1022] Sum of Root To Leaf Binary Numbers

https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/

* algorithms
* Easy (56.27%)
* Source Code:       1022.sum-of-root-to-leaf-binary-numbers.py
* Total Accepted:    13.5K
* Total Submissions: 23.8K
* Testcase Example:  '[1,0,1,0,1,0,1]'

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

 

Example 1:




Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


 

Note:


        The number of nodes in the tree is between 1 and 1000.
        node.val is 0 or 1.
        The answer will not exceed 2^31 - 1.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        lst = []
        def findpath(root,s):
            if not root.left and not root.right:
                lst.append(s+str(root.val))
            else:
                if root.left:
                    findpath(root.left,s+str(root.val))
                if root.right:
                    findpath(root.right,s+str(root.val))
        findpath(root,"")
        return sum([int(x,2) for x in lst])

        
