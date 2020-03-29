#
# @lc app=leetcode id=423 lang=python
#
# [423] Reconstruct Original Digits from English
#
# https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
#
# algorithms
# Medium (45.84%)
# Likes:    152
# Dislikes: 519
# Total Accepted:    22.4K
# Total Submissions: 48.2K
# Testcase Example:  '"owoztneoer"'
#
# Given a non-empty string containing an out-of-order English representation of
# digits 0-9, output the digits in ascending order.
# 
# Note:
# 
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original
# digits. That means invalid inputs such as "abc" or "zerone" are not
# permitted.
# Input length is less than 50,000.
# 
# 
# 
# Example 1:
# 
# Input: "owoztneoer"
# 
# Output: "012"
# 
# 
# 
# Example 2:
# 
# Input: "fviefuro"
# 
# Output: "45"
# 
# 
#

# @lc code=start
import collections


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_cnts = collections.Counter(s)
        nums = ['six', 'zero', "two", "eight", "seven", "four", "five", "one", "three", "nine"]
        num_cnts = [collections.Counter(letter) for letter in nums]
        digits = [6, 0, 2, 8, 7, 4, 5, 1, 3, 9]
        ans = [""] * 10
        for idx, num in enumerate(nums):
            num_cnt = num_cnts[idx]
            t = min([s_cnts[c] / num_cnt[c] for c in num_cnt])
            ans[digits[idx]] = t
            for i in range(t):
                s_cnts.subtract(num_cnt)
        return "".join(str(i) * n for i, n in enumerate(ans))

# @lc code=end
