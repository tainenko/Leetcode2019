# Given a string text, you want to use the characters of text to form as many 
# instances of the word "balloon" as possible. 
# 
#  You can use each character in text at most once. Return the maximum number 
# of instances that can be formed. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: text = "nlaebolko"
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: text = "loonbalxballpoon"
# Output: 2
#  
# 
#  Example 3: 
# 
#  
# Input: text = "leetcode"
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= text.length <= 10⁴ 
#  text consists of lower case English letters only. 
#  
#  Related Topics Hash Table String Counting 👍 941 👎 66


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count.get('b', 0), count.get('a', 0), count.get('l', 0) // 2, count.get('o', 0) // 2,
                   count.get('n', 0))
# leetcode submit region end(Prohibit modification and deletion)
