# We can shift a string by shifting each of its letters to its successive 
# letter. 
# 
#  
#  For example, "abc" can be shifted to be "bcd". 
#  
# 
#  We can keep shifting the string to form a sequence. 
# 
#  
#  For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" 
# -> ... -> "xyz". 
#  
# 
#  Given an array of strings strings, group all strings[i] that belong to the 
# same shifting sequence. You may return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
#  Example 2: 
#  Input: strings = ["a"]
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= strings.length <= 200 
#  1 <= strings[i].length <= 50 
#  strings[i] consists of lowercase English letters. 
#  
#  Related Topics Array Hash Table String 👍 1083 👎 201


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strings:
            key = tuple((ord(word[i]) - ord(word[0]) + 26) % 26 for i in range(len(word)))
            res[key].append(word)

        return res.values()

# leetcode submit region end(Prohibit modification and deletion)
