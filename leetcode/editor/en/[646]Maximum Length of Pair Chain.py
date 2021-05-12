# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and l
# efti < righti.
#
#  A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can
# be formed in this fashion.
#
#  Return the length longest chain which can be formed.
#
#  You do not need to use up all the given intervals. You can select pairs in an
# y order.
#
#
#  Example 1:
#
#
# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
#
#
#  Example 2:
#
#
# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
#
#
#
#  Constraints:
#
#
#  n == pairs.length
#  1 <= n <= 1000
#  -1000 <= lefti < righti < 1000
#
#  Related Topics Dynamic Programming
#  👍 1388 👎 89


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: (x[1], x[0]))
        length = 0
        prev = float('-inf')
        for start, end in pairs:
            if prev < start:
                length += 1
                prev = end
        return length
# leetcode submit region end(Prohibit modification and deletion)
