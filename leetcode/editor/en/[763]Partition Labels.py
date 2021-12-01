# You are given a string s. We want to partition the string into as many parts 
# as possible so that each letter appears in at most one part. 
# 
#  Return a list of integers representing the size of these parts. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it 
# splits s into less parts.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "eccbbbbdec"
# Output: [10]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 500 
#  s consists of lowercase English letters. 
#  
#  Related Topics Hash Table Two Pointers String Greedy 👍 5852 👎 237


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = collections.defaultdict(lambda: [-1, -1])
        for idx, char in enumerate(s):
            idx_map = m[char]
            if idx_map[0] == -1:
                idx_map[0] = idx
            idx_map[1] = idx
        intervals = [(start, end) for start, end in m.values()]
        intervals.sort(key=lambda x: x[0])
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i, j in intervals[1:]:
            if end > i:
                end = max(j, end)
            else:
                res.append((start, end))
                start = i
                end = j
        if not res or res[-1] != (start, end):
            res.append((start, end))
        return [right - left + 1 for left, right in res]
# leetcode submit region end(Prohibit modification and deletion)
