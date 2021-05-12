# Given a string s, return the number of palindromic substrings in it.
#
#  A string is a palindrome when it reads the same backward as forward.
#
#  A substring is a contiguous sequence of characters within the string.
#
#
#  Example 1:
#
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
#
#  Example 2:
#
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 1000
#  s consists of lowercase English letters.
#
#  Related Topics String Dynamic Programming
#  👍 4275 👎 138


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res += self.helper(s, i, i)
            res += self.helper(s, i, i + 1)
        return res

    def helper(self, s, left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            res += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
