#
# @lc app=leetcode id=433 lang=python
#
# [433] Minimum Genetic Mutation
#
# https://leetcode.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (40.83%)
# Likes:    360
# Dislikes: 47
# Total Accepted:    28.8K
# Total Submissions: 70.5K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# A gene string can be represented by an 8-character long string, with choices
# from "A", "C", "G", "T".
# 
# Suppose we need to investigate about a mutation (mutation from "start" to
# "end"), where ONE mutation is defined as ONE single character changed in the
# gene string.
# 
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
# 
# Also, there is a given gene "bank", which records all the valid gene
# mutations. A gene must be in the bank to make it a valid gene string.
# 
# Now, given 3 things - start, end, bank, your task is to determine what is the
# minimum number of mutations needed to mutate from "start" to "end". If there
# is no such a mutation, return -1.
# 
# Note:
# 
# 
# Starting point is assumed to be valid, so it might not be included in the
# bank.
# If multiple mutations are needed, all mutations during in the sequence must
# be valid.
# You may assume start and end string is not the same.
# 
# 
# 
# 
# Example 1:
# 
# 
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# return: 1
# 
# 
# 
# 
# Example 2:
# 
# 
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# return: 2
# 
# 
# 
# 
# Example 3:
# 
# 
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# return: 3
# 
# 
# 
# 
#

# @lc code=start
import collections


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bfs = collections.deque()
        bank = set(bank)
        bfs.append((start, 0))
        while bfs:
            gene, step = bfs.popleft()
            if gene == end:
                return step
            for i in range(len(gene)):
                for letter in "ACGT":
                    newGene = gene[:i] + letter + gene[i + 1:]
                    if newGene in bank:
                        bfs.append((newGene, step + 1))
                        bank.remove(newGene)
        return -1

# @lc code=end
