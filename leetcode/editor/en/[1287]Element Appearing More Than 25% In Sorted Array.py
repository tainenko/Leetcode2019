# Given an integer array sorted in non-decreasing order, there is exactly one in
# teger in the array that occurs more than 25% of the time, return that integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [1,1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 104 
#  0 <= arr[i] <= 105 
#  
#  Related Topics Array 
#  👍 526 👎 34

from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnts = Counter(arr)
        return sorted([(num, time) for num, time in cnts.items()], key=lambda x: x[1])[-1][0]

    # leetcode submit region end(Prohibit modification and deletion)
