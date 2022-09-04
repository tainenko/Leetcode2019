# A distinct string is a string that is present only once in an array. 
# 
#  Given an array of strings arr, and an integer k, return the kᵗʰ distinct 
# string present in arr. If there are fewer than k distinct strings, return an empty 
# string "". 
# 
#  Note that the strings are considered in the order in which they appear in 
# the array. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = ["d","b","c","b","c","a"], k = 2
# Output: "a"
# Explanation:
# The only distinct strings in arr are "d" and "a".
# "d" appears 1ˢᵗ, so it is the 1ˢᵗ distinct string.
# "a" appears 2ⁿᵈ, so it is the 2ⁿᵈ distinct string.
# Since k == 2, "a" is returned. 
#  
# 
#  Example 2: 
# 
#  
# Input: arr = ["aaa","aa","a"], k = 1
# Output: "aaa"
# Explanation:
# All strings in arr are distinct, so the 1ˢᵗ string "aaa" is returned.
#  
# 
#  Example 3: 
# 
#  
# Input: arr = ["a","b","a"], k = 3
# Output: ""
# Explanation:
# The only distinct string is "b". Since there are fewer than 3 distinct 
# strings, we return an empty string "".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= arr.length <= 1000 
#  1 <= arr[i].length <= 5 
#  arr[i] consists of lowercase English letters. 
#  
# 
#  Related Topics Array Hash Table String Counting 👍 424 👎 12


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt = Counter(arr)
        distincts = [k for k, v in cnt.items() if v == 1]
        if k > len(distincts):
            return ""
        return distincts[k - 1]

# leetcode submit region end(Prohibit modification and deletion)
