# You are given an array of digits called digits. Your task is to determine the 
# number of distinct three-digit even numbers that can be formed using these 
# digits. 
# 
#  Note: Each copy of a digit can only be used once per number, and there may 
# not be leading zeros. 
# 
#  
#  Example 1: 
# 
#  
#  Input: digits = [1,2,3,4] 
#  
# 
#  Output: 12 
# 
#  Explanation: The 12 distinct 3-digit even numbers that can be formed are 124,
#  132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 
# cannot be formed because there is only 1 copy of the digit 2. 
# 
#  Example 2: 
# 
#  
#  Input: digits = [0,2,2] 
#  
# 
#  Output: 2 
# 
#  Explanation: The only 3-digit even numbers that can be formed are 202 and 220
# . Note that the digit 2 can be used twice because it appears twice in the array.
#  
# 
#  Example 3: 
# 
#  
#  Input: digits = [6,6,6] 
#  
# 
#  Output: 1 
# 
#  Explanation: Only 666 can be formed. 
# 
#  Example 4: 
# 
#  
#  Input: digits = [1,3,5] 
#  
# 
#  Output: 0 
# 
#  Explanation: No even 3-digit numbers can be formed. 
# 
#  
#  Constraints: 
# 
#  
#  3 <= digits.length <= 10 
#  0 <= digits[i] <= 9 
#  
# 
#  Related Topics Array Hash Table Recursion Enumeration 👍 59 👎 20


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNumbers2(self, digits: List[int]) -> int:
        digits = Counter(digits)
        cnt = 0
        for num in range(100, 999, 2):
            for k, v in Counter(str(num)).items():
                if digits[int(k)] >= v:
                    continue
                break
            else:
                cnt += 1
        return cnt

    def totalNumbers(self, digits: List[int]) -> int:
        res = set()
        for i, u in enumerate(digits):
            if u & 1:
                continue
            for j, v in enumerate(digits):
                if i == j:
                    continue
                for k, w in enumerate(digits):
                    if k == i or k == j:
                        continue
                    if w == 0:
                        continue
                    res.add(w * 100 + v * 10 + u)
        return len(res)
# leetcode submit region end(Prohibit modification and deletion)
