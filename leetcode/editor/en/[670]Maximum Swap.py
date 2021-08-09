# You are given an integer num. You can swap two digits at most once to get the 
# maximum valued number. 
# 
#  Return the maximum valued number you can get. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
#  
#
#  Example 2: 
# 
#  
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= num <= 108 
#  
#  Related Topics Math Greedy 
#  👍 1701 👎 98


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = list(str(num))
        mx = len(nums) - 1
        pos1 = -1
        pos2 = -1
        for i in range(len(nums) - 2, -1, -1):
            if int(nums[i]) < int(nums[mx]):
                pos1 = i
                pos2 = mx
            elif int(nums[i]) > int(nums[mx]):
                mx = i
        if pos1 != -1:
            nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
        return int("".join(nums))

# leetcode submit region end(Prohibit modification and deletion)
