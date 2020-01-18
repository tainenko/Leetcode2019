#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (45.84%)
# Likes:    2315
# Dislikes: 122
# Total Accepted:    158.4K
# Total Submissions: 332.3K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# Examples:
# 
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
# 
# 
# 
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.helper(s,[0])

    def helper(self, s, nums):
        res = ""
        n = len(s)
        while nums[0] < n and s[nums[0]] != ']':
            if s[nums[0]].isalpha():
                res += s[nums[0]]
                nums[0] = nums[0]+1
            else:
                cnt = ""
                while s[nums[0]].isdigit():
                    cnt += s[nums[0]]
                    nums[0] = nums[0]+1
                nums[0] = nums[0]+1
                t = self.helper(s, nums)
                nums[0] = nums[0]+1
                if cnt:
                    res = res + int(cnt) * t
        return res

    def decodeString_iter(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = 0
        tmp = ""
        nums = []
        ss = []
        for char in s:
            if char == "[":
                nums.append(cnt)
                cnt = 0
                ss.append(tmp)
                tmp = ""
            elif char == "]":
                tmp = ss.pop() + tmp * nums.pop()
            elif char.isdigit():
                cnt = 10 * cnt + int(char)
            else:
                tmp += char
        return ss[-1] if ss else tmp

# @lc code=end
