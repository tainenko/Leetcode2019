#
# @lc app=leetcode id=341 lang=python
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (48.79%)
# Likes:    1245
# Dislikes: 521
# Total Accepted:    137.2K
# Total Submissions: 272.8K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, implement an iterator to flatten it.
# 
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
# 
# Example 1:
# 
# 
# 
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns
# false, 
# the order of elements returned by next should be: [1,1,2,1,1].
# 
# 
# Example 2:
# 
# 
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns
# false, 
# the order of elements returned by next should be: [1,4,6].
# 
# 
# 
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
import collections


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flatten_list = []
        self._flatten(nestedList, self.flatten_list)
        self.index = -1

    def _flatten(self, nestedList, lst):
        for ele in nestedList:
            if not ele.isInteger():
                self._flatten(ele.getList(),lst)
                continue
            lst.append(ele)

    def next(self):
        """
        :rtype: int
        """
        while self.hasNext():
            self.index += 1
            return self.flatten_list[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index + 1 < len(self.flatten_list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
