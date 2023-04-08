# You are given a string s representing a list of words. Each letter in the 
# word has one or more options. 
# 
#  
#  If there is one option, the letter is represented as is. 
#  If there is more than one option, then curly braces delimit the options. For 
# example, "{a,b,c}" represents options ["a", "b", "c"]. 
#  
# 
#  For example, if s = "a{b,c}", the first character is always 'a', but the 
# second character can be 'b' or 'c'. The original list is ["ab", "ac"]. 
# 
#  Return all words that can be formed in this manner, sorted in 
# lexicographical order. 
# 
#  
#  Example 1: 
#  Input: s = "{a,b}c{d,e}f"
# Output: ["acdf","acef","bcdf","bcef"]
#  
#  Example 2: 
#  Input: s = "abcd"
# Output: ["abcd"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 50 
#  s consists of curly brackets '{}', commas ',', and lowercase English letters.
#  
#  s is guaranteed to be a valid input. 
#  There are no nested curly brackets. 
#  All characters inside a pair of consecutive opening and ending curly 
# brackets are different. 
#  
# 
#  Related Topics String Backtracking Breadth-First Search 👍 599 👎 49


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def expand(self, s: str) -> List[str]:
        res = [""]
        i = 0
        while i < len(s):
            if s[i] != "{":
                for j in range(len(res)):
                    res[j] += s[i]
                i += 1
                continue

            j = i
            while s[j] != "}":
                j += 1
            chars = []
            for char in s[i + 1:j]:
                if char == ",":
                    continue
                chars.append(char)
            chars.sort()
            res = [word + char for word in res for char in chars]
            i = j + 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
