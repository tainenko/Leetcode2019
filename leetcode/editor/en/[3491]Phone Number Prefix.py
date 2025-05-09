# You are given a string array numbers that represents phone numbers. Return 
# true if no phone number is a prefix of any other phone number; otherwise, return 
# false. 
# 
#  
#  Example 1: 
# 
#  
#  Input: numbers = ["1","2","4","3"] 
#  
# 
#  Output: true 
# 
#  Explanation: 
# 
#  No number is a prefix of another number, so the output is true. 
# 
#  Example 2: 
# 
#  
#  Input: numbers = ["001","007","15","00153"] 
#  
# 
#  Output: false 
# 
#  Explanation: 
# 
#  The string "001" is a prefix of the string "00153". Thus, the output is 
# false. 
# 
#  
#  Constraints: 
# 
#  
#  2 <= numbers.length <= 50 
#  1 <= numbers[i].length <= 50 
#  All numbers contain only digits '0' to '9'. 
#  
# 
#  Related Topics Array String Trie Sorting 👍 4 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def phonePrefix(self, numbers: List[str]) -> bool:
        numbers.sort()
        trie = dict()
        for num in numbers:
            node = trie
            for n in num:
                if n not in node:
                    node[n] = dict()
                node = node[n]
                if "$" in node:
                    return False
            node["$"] = dict()
        return True

    def brue_force(self, numbers: List[str]) -> bool:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[j].startswith(numbers[i]):
                    return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
