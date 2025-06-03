# Given a string s, return the maximum number of unique substrings that the 
# given string can be split into. 
# 
#  You can split string s into any list of non-empty substrings, where the 
# concatenation of the substrings forms the original string. However, you must split 
# the substrings such that all of them are unique. 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ababccc"
# Output: 5
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. 
# Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' 
# multiple times.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "aba"
# Output: 2
# Explanation: One way to split maximally is ['a', 'ba'].
#  
# 
#  Example 3: 
# 
#  
# Input: s = "aa"
# Output: 1
# Explanation: It is impossible to split the string any further.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 16 
#  s contains only lower case English letters. 
#  
# 
#  Related Topics Hash Table String Backtracking 👍 1483 👎 74


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(i: int):
            nonlocal ans
            if len(st) + len(s) - i <= ans:
                return
            if i >= len(s):
                ans = max(ans, len(st))
                return
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in st:
                    continue
                st.add(s[i:j])
                dfs(j)
                st.remove(s[i:j])

        ans = 0
        st = set()
        dfs(0)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
