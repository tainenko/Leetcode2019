# An integer has sequential digits if and only if each digit in the number is 
# one more than the previous digit. 
# 
#  Return a sorted list of all the integers in the range [low, high] inclusive 
# that have sequential digits. 
# 
#  
#  Example 1: 
#  Input: low = 100, high = 300
# Output: [123,234]
#  Example 2: 
#  Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
#  
#  
#  Constraints: 
# 
#  
#  10 <= low <= high <= 10^9 
#  
#  Related Topics Enumeration 👍 1208 👎 84


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(i, 10):
                num = int(''.join([str(j - i + k + 1) for k in range(i)]))
                if low <= num <= high:
                    res.append(num)
        return res
# leetcode submit region end(Prohibit modification and deletion)
