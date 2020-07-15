#
# @lc app=leetcode id=522 lang=python
#
# [522] Longest Uncommon Subsequence II
#
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/
#
# algorithms
# Medium (33.66%)
# Likes:    168
# Dislikes: 573
# Total Accepted:    21.7K
# Total Submissions: 64.1K
# Testcase Example:  '["aba","cdc","eae"]'
#
# 
# Given a list of strings, you need to find the longest uncommon subsequence
# among them. The longest uncommon subsequence is defined as the longest
# subsequence of one of these strings and this subsequence should not be any
# subsequence of the other strings.
# 
# 
# 
# A subsequence is a sequence that can be derived from one sequence by deleting
# some characters without changing the order of the remaining elements.
# Trivially, any string is a subsequence of itself and an empty string is a
# subsequence of any string.
# 
# 
# 
# The input will be a list of strings, and the output needs to be the length of
# the longest uncommon subsequence. If the longest uncommon subsequence doesn't
# exist, return -1.
# 
# 
# Example 1:
# 
# Input: "aba", "cdc", "eae"
# Output: 3
# 
# 
# 
# Note:
# 
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].
# 
# 
#

# @lc code=start
import collections


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = -1
        for i in range(len(strs)):
            for j in range(len(strs)):
                if i == j:
                    continue
                if self.isSubsequence(strs[i], strs[j]):
                    break
            else:
                res = max(res, len(strs[i]))
        return res

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        queue = collections.deque(s)
        for c in t:
            if not queue: return True
            if c == queue[0]:
                queue.popleft()
        return not queue
# @lc code=end
