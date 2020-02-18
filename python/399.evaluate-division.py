#
# @lc app=leetcode id=399 lang=python
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (48.28%)
# Likes:    1816
# Dislikes: 140
# Total Accepted:    108.2K
# Total Submissions: 217K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
#  '[2.0,3.0]\n' +
#  '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# According to the example above:
# 
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#

# @lc code=start
from collections import deque


class Solution(object):

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        def find(x):
            if x != U[x][0]:
                px, py = find(U[x][0])
                U[x] = (px, U[x][1] * py)
            return U[x]

        def devide(x, y):
            rx, vx = find(x)
            ry, vy = find(y)
            if rx != ry:
                return -1
            else:
                return vx / vy

        U = {}
        for (x, y), v in zip(equations, values):
            if x not in U and y not in U:
                U[x] = (y, v)
                U[y] = (y, 1.0)
            elif x not in U:
                U[x] = (y, v)
            elif y not in U:
                U[y] = (x, 1.0 / v)
            else:
                rx, vx = find(x)
                ry, vy = find(y)
                U[rx] = (ry, v / vx * vy)
        ans = [devide(x, y) if x in U and y in U else -1 for x, y in queries]
        return ans

# @lc code=end
