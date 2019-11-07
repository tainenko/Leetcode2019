#
# @lc app=leetcode id=274 lang=python
#
# [274] H-Index
#
# https://leetcode.com/problems/h-index/description/
#
# algorithms
# Medium (34.81%)
# Likes:    463
# Dislikes: 791
# Total Accepted:    134.4K
# Total Submissions: 383.9K
# Testcase Example:  '[3,0,6,1,5]'
#
# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
# 
# According to the definition of h-index on Wikipedia: "A scientist has index h
# if h of his/her N papers have at least h citations each, and the other N − h
# papers have no more than h citations each."
# 
# Example:
# 
# 
# Input: citations = [3,0,6,1,5]
# Output: 3 
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each
# of them had 
# ⁠            received 3, 0, 6, 1, 5 citations respectively. 
# Since the researcher has 3 papers with at least 3 citations each and the
# remaining 
# two with no more than 3 citations each, her h-index is 3.
# 
# Note: If there are several possible values for h, the maximum one is taken as
# the h-index.
# 
#

# @lc code=start
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count = [0] * (len(citations) + 1)
        for i in range(len(citations)):
            if citations[i] >= len(citations):
                count[len(citations)] += 1
            else:
                count[citations[i]] += 1
        for j in range(len(citations), -1, -1):
            if count[j] >= j:
                return j
            count[j - 1] += count[j]

    def hIndex_sort(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        level = 0
        citations.sort()
        for i in range(len(citations)):
            level = max(level, min(len(citations) - i, citations[i]))
        return level

# @lc code=end
