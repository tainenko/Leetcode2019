#
# @lc app=leetcode id=1108 lang=python
#
# [1108] Defanging an IP Address
#
# https://leetcode.com/problems/defanging-an-ip-address/description/
#
# algorithms
# Easy (86.15%)
# Total Accepted:    25.4K
# Total Submissions: 29.5K
# Testcase Example:  '"1.1.1.1"'
#
# Given a valid (IPv4) IP address, return a defanged version of that IP
# address.
# 
# A defanged IP address replaces every period "." with "[.]".
# 
# 
# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"
# 
# 
# Constraints:
# 
# 
# The given address is a valid IPv4 address.
# 
#
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace('.','[.]')
