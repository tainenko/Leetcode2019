# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. 
#
# Example: 
#
# 
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
# 
# Related Topics Hash Table Bit Manipulation


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()
        for i in range(0, len(s) - 9):
            curr = s[i:i + 10]
            if curr in seen:
                repeated.add(curr)
            seen.add(curr)
        return list(repeated)

# leetcode submit region end(Prohibit modification and deletion)
