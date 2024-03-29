# In some array arr, the values were in arithmetic progression: the values arr[
# i + 1] - arr[i] are all equal for every 0 <= i < arr.length - 1. 
# 
#  A value from arr was removed that was not the first or last value in the 
# array. 
# 
#  Given arr, return the removed value. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [5,7,11,13]
# Output: 9
# Explanation: The previous array was [5,7,9,11,13].
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [15,13,12]
# Output: 14
# Explanation: The previous array was [15,14,13,12]. 
# 
#  
#  Constraints: 
# 
#  
#  3 <= arr.length <= 1000 
#  0 <= arr[i] <= 10⁵ 
#  The given array is guaranteed to be a valid array. 
#  
#  Related Topics Array Math 👍 230 👎 30


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1] - arr[0]) // len(arr)
        if diff == 0:
            return arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == diff:
                continue
            return arr[i] + diff
# leetcode submit region end(Prohibit modification and deletion)
