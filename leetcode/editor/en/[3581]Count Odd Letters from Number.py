# You are given an integer n perform the following steps: 
# 
#  
#  Convert each digit of n into its lowercase English word (e.g., 4 → "four", 1 
# → "one"). 
#  Concatenate those words in the original digit order to form a string s. 
#  
# 
#  Return the number of distinct characters in s that appear an odd number of 
# times. 
# 
#  
#  Example 1: 
# 
#  
#  Input: n = 41 
#  
# 
#  Output: 5 
# 
#  Explanation: 
# 
#  41 → "fourone" 
# 
#  Characters with odd frequencies: 'f', 'u', 'r', 'n', 'e'. Thus, the answer 
# is 5. 
# 
#  Example 2: 
# 
#  
#  Input: n = 20 
#  
# 
#  Output: 5 
# 
#  Explanation: 
# 
#  20 → "twozero" 
# 
#  Characters with odd frequencies: 't', 'w', 'z', 'e', 'r'. Thus, the answer 
# is 5. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 10⁹ 
#  
# 
#  Related Topics Hash Table String Simulation Counting 👍 1 👎 1


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countOddLetters(self, n: int) -> int:
        maps = {
            "1": "one",
            "2": "two",
            "3": "three",
            "4": "four",
            "5": "five",
            "6": "six",
            "7": "seven",
            "8": "eight",
            "9": "nine",
            "0": "zero",
        }
        cnt = Counter("".join([maps[num] for num in str(n)]))
        return sum([1 for v in cnt.values() if v % 2])

# leetcode submit region end(Prohibit modification and deletion)
