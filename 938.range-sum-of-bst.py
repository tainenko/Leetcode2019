'''
[938] Range Sum of BST

https://leetcode.com/problems/range-sum-of-bst/description/

* algorithms
* Medium (80.37%)
* Source Code:       938.range-sum-of-bst.py
* Total Accepted:    48.3K
* Total Submissions: 60.6K
* Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

 


Example 1:


Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32



Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


 

Note:


        The number of nodes in the tree is at most 10000.
        The final answer is guaranteed to be less than 2^31.


'''
#Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(node):
            if node:
                if L<=node.val<=R:
                    self.total+=node.val
                if L<node.val:
                    dfs(node.left)
                if node.val<R:
                    dfs(node.right)
        self.total=0
        dfs(root)
        return self.total
