#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (32.15%)
# Total Accepted:    149.1K
# Total Submissions: 463.2K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
# 
# Example:
# 
# 
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
# 
# 
#
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        '255,255,255,255'
        '0,0,0,0'
        res = []
        self.dfs(res, [], s)
        return res

    def dfs(self, res, list, s):
        if len(s) > (4 - len(list)) * 3:
            return
        if len(list) == 4 and not s:
            res.append('.'.join(list))
        for i in range(min(3, len(s))):
            tmp = s[:i + 1]
            if not self.isvalid(tmp):
                continue
            self.dfs(res, list + [tmp], s[i + 1:])

    def isvalid(self, s):
        if s[0] == '0':
            return s == '0'
        else:
            return 0 <= int(s) <= 255
