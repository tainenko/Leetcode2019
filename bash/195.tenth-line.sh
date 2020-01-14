#
# @lc app=leetcode id=195 lang=bash
#
# [195] Tenth Line
#
# https://leetcode.com/problems/tenth-line/description/
#
# shell
# Easy (33.85%)
# Likes:    144
# Dislikes: 143
# Total Accepted:    46.6K
# Total Submissions: 138.2K
# Testcase Example:  'Line 1\\nLine 2\\nLine 3\\nLine 4\\nLine 5\\nLine 6\\nLine 7\\nLine 8\\nLine 9\\nLine 10'
#
# Given a text file file.txt, print just the 10th line of the file.
# 
# Example:
# 
# Assume that file.txt has the following content:
# 
# 
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10
# 
# 
# Your script should output the tenth line, which is:
# 
# 
# Line 10
# 
# 
# Note:
# 1. If the file contains less than 10 lines, what should you output?
# 2. There's at least three different solutions. Try to explore all
# possibilities.
# 
#

# @lc code=start
# Read from the file file.txt and output the tenth line to stdout.
tail -n+10 file.txt | head -n1
# @lc code=end

