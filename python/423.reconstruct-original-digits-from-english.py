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
        cnts = collections.Counter(s)
        nums = ['six', 'zero', "two", "eight", "seven", "four", "five", "one", "three", "nine"]
        # digits = [6, 0, 2, 8, 7, 4, 5, 1, 3, 9]
        digits = [0] * 10
        digits[6] = cnts["x"]
        digits[0] = cnts["z"]
        digits[2] = cnts["w"]
        digits[8] = cnts["g"]
        digits[7] = cnts["s"] - digits[6]
        digits[5] = cnts["v"] - digits[7]
        digits[3] = cnts["h"] - digits[8]
        digits[4] = cnts["f"] - digits[5]
        digits[1] = cnts["o"] - digits[4] - digits[2] - digits[0]
        digits[9] = cnts["i"] - digits[6] - digits[8] - digits[5]
        return "".join([str(index) * value for index, value in enumerate(digits) if value > 0])

# @lc code=end
