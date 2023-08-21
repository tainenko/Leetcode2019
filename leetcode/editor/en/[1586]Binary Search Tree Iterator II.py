# Implement the BSTIterator class that represents an iterator over the in-order 
# traversal of a binary search tree (BST): 
# 
#  
#  BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. 
# The root of the BST is given as part of the constructor. The pointer should be 
# initialized to a non-existent number smaller than any element in the BST. 
#  boolean hasNext() Returns true if there exists a number in the traversal to 
# the right of the pointer, otherwise returns false. 
#  int next() Moves the pointer to the right, then returns the number at the 
# pointer. 
#  boolean hasPrev() Returns true if there exists a number in the traversal to 
# the left of the pointer, otherwise returns false. 
#  int prev() Moves the pointer to the left, then returns the number at the 
# pointer. 
#  
# 
#  Notice that by initializing the pointer to a non-existent smallest number, 
# the first call to next() will return the smallest element in the BST. 
# 
#  You may assume that next() and prev() calls will always be valid. That is, 
# there will be at least a next/previous number in the in-order traversal when next(
# )/prev() is called. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input
# ["BSTIterator", "next", "next", "prev", "next", "hasNext", "next", "next", 
# "next", "hasNext", "hasPrev", "prev", "prev"]
# [[[7, 3, 15, null, null, 9, 20]], [null], [null], [null], [null], [null], [
# null], [null], [null], [null], [null], [null], [null]]
# Output
# [null, 3, 7, 3, 7, true, 9, 15, 20, false, true, 15, 9]
# 
# Explanation
# // The underlined element is where the pointer currently is.
# BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]); // 
# state is   [3, 7, 9, 15, 20]
# bSTIterator.next(); // state becomes [3, 7, 9, 15, 20], return 3
# bSTIterator.next(); // state becomes [3, 7, 9, 15, 20], return 7
# bSTIterator.prev(); // state becomes [3, 7, 9, 15, 20], return 3
# bSTIterator.next(); // state becomes [3, 7, 9, 15, 20], return 7
# bSTIterator.hasNext(); // return true
# bSTIterator.next(); // state becomes [3, 7, 9, 15, 20], return 9
# bSTIterator.next(); // state becomes [3, 7, 9, 15, 20], return 15
# bSTIterator.next(); // state becomes [3, 7, 9, 15, 20], return 20
# bSTIterator.hasNext(); // return false
# bSTIterator.hasPrev(); // return true
# bSTIterator.prev(); // state becomes [3, 7, 9, 15, 20], return 15
# bSTIterator.prev(); // state becomes [3, 7, 9, 15, 20], return 9
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁵]. 
#  0 <= Node.val <= 10⁶ 
#  At most 10⁵ calls will be made to hasNext, next, hasPrev, and prev. 
#  
# 
#  
# Follow up: Could you solve the problem without precalculating the values of 
# the tree?
# 
#  Related Topics Stack Tree Design Binary Search Tree Binary Tree Iterator 👍 2
# 52 👎 31


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.next_stack = []
        self.prev_stack = []
        self.idx = 0
        while root:
            self.next_stack.append(root)
            root = root.left

    def hasNext(self) -> bool:
        return len(self.next_stack) > 0 or (self.idx + 1) < len(self.prev_stack)

    def next(self) -> int:
        if self.idx + 1 < len(self.prev_stack):
            self.idx += 1
            return self.prev_stack[self.idx].val
        node = self.next_stack.pop()
        self.prev_stack.append(node)
        self.idx = len(self.prev_stack) - 1

        curr = node.right
        while curr:
            self.next_stack.append(curr)
            curr = curr.left
        return node.val

    def hasPrev(self) -> bool:
        return self.idx != 0

    def prev(self) -> int:
        self.idx -= 1
        return self.prev_stack[self.idx].val

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()
# leetcode submit region end(Prohibit modification and deletion)
