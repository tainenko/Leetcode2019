# There is a room with n bulbs labeled from 1 to n that all are turned on initia
# lly, and four buttons on the wall. Each of the four buttons has a different func
# tionality where: 
# 
#  
#  Button 1: Flips the status of all the bulbs. 
#  Button 2: Flips the status of all the bulbs with even labels (i.e., 2, 4, ...
# ). 
#  Button 3: Flips the status of all the bulbs with odd labels (i.e., 1, 3, ...)
# . 
#  Button 4: Flips the status of all the bulbs with a label j = 3k + 1 where k =
#  0, 1, 2, ... (i.e., 1, 4, 7, 10, ...). 
#  
# 
#  You will press one of the four mentioned buttons exactly presses times. 
# 
#  Given the two integers n and presses, return the number of different statuses
#  after pressing the four buttons exactly presses times. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 1, presses = 1
# Output: 2
# Explanation: Status can be: [on], [off].
#  
# 
#  Example 2: 
# 
#  
# Input: n = 2, presses = 1
# Output: 3
# Explanation: Status can be: [on, off], [off, on], [off, off].
#  
# 
#  Example 3: 
# 
#  
# Input: n = 3, presses = 1
# Output: 4
# Explanation: Status can be: [off, on, off], [on, off, on], [off, off, off], [o
# ff, on, on].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1000 
#  0 <= presses <= 1000 
#  
#  Related Topics Math Bit Manipulation Depth-First Search Breadth-First Search 
# 
#  👍 184 👎 1043


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        
# leetcode submit region end(Prohibit modification and deletion)
