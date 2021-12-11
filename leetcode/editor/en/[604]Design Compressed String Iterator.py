# Design and implement a data structure for a compressed string iterator. The 
# given compressed string will be in the form of each letter followed by a positive 
# integer representing the number of this letter existing in the original 
# uncompressed string. 
# 
#  Implement the StringIterator class: 
# 
#  
#  next() Returns the next character if the original string still has 
# uncompressed characters, otherwise returns a white space. 
#  hasNext() Returns true if there is any letter needs to be uncompressed in 
# the original string, otherwise returns false. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", 
# "next", "hasNext"]
# [["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
# Output
# [null, "L", "e", "e", "t", "C", "o", true, "d", true]
# 
# Explanation
# StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
# stringIterator.next(); // return "L"
# stringIterator.next(); // return "e"
# stringIterator.next(); // return "e"
# stringIterator.next(); // return "t"
# stringIterator.next(); // return "C"
# stringIterator.next(); // return "o"
# stringIterator.hasNext(); // return True
# stringIterator.next(); // return "d"
# stringIterator.hasNext(); // return True
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= compressedString.length <= 1000 
#  compressedString consists of lower-case an upper-case English letters and 
# digits. 
#  The number of a single character repetitions in compressedString is in the 
# range [1, 10^9] 
#  At most 100 calls will be made to next and hasNext. 
#  
#  Related Topics Array Hash Table String Design Iterator 👍 330 👎 117


# leetcode submit region begin(Prohibit modification and deletion)
from typing import Tuple


class StringIterator:

    def __init__(self, compressedString: str):
        self.idx = 0
        self.s = compressedString
        self.letter, self.cnt = self.helper()
        self.curr = 0

    def helper(self) -> Tuple[str, int]:
        if self.idx >= len(self.s) - 1:
            return " ", -1
        self.curr = 0
        char = self.s[self.idx]
        num = ""
        self.idx += 1
        while self.idx < len(self.s) and self.s[self.idx].isdigit():
            num += self.s[self.idx]
            self.idx += 1
        return char, int(num)

    def next(self) -> str:
        if self.letter == " ":
            return " "
        if self.curr >= self.cnt:
            self.curr = 0
            self.letter, self.cnt = self.helper()
        self.curr += 1
        return self.letter

    def hasNext(self) -> bool:
        return self.idx < len(self.s) or self.curr < self.cnt

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# leetcode submit region end(Prohibit modification and deletion)
