# Given a list of strings dict where all the strings are of the same length. 
# 
#  Return true if there are 2 strings that only differ by 1 character in the 
# same index, otherwise return false. 
# 
#  
#  Example 1: 
# 
#  
# Input: dict = ["abcd","acbd", "aacd"]
# Output: true
# Explanation: Strings "abcd" and "aacd" differ only by one character in the 
# index 1.
#  
# 
#  Example 2: 
# 
#  
# Input: dict = ["ab","cd","yz"]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: dict = ["abcd","cccc","abyd","abab"]
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of characters in dict <= 10⁵ 
#  dict[i].length == dict[j].length 
#  dict[i] should be unique. 
#  dict[i] contains only lowercase English letters. 
#  
# 
#  
#  Follow up: Could you solve this problem in O(n * m) where n is the length of 
# dict and m is the length of each string. 
# 
#  Related Topics Hash Table String Rolling Hash Hash Function 👍 347 👎 83


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        # rolling hash
        N, M = len(dict), len(dict[0])
        MOD = 1000000007
        BASE = 27
        memo = set()

        def helper(char: str):
            if char == "*":
                return 26
            return ord(char) - ord('a')

        def collision(word1, word2):
            cnt = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    cnt += 1
            return cnt == 1

        # time: O(N * M)
        # space: O(N)
        arr = []
        for word in dict:
            hash_value = 0
            for i, char in enumerate(word):
                hash_value = ((hash_value * BASE) % MOD + helper(char)) % MOD
            arr.append(hash_value)

        # time: O(N * M)
        # space: O(N * M)
        memo = {}
        for idx, word in enumerate(dict):
            base = 1
            hash_value = arr[idx]
            for i in range(M - 1, -1, -1):
                new_hash_value = (hash_value + base * (helper("*") - helper(word[i]))) % MOD
                if new_hash_value in memo:
                    # collision test
                    if collision(word, dict[memo[new_hash_value]]):
                        return True
                memo[new_hash_value] = idx
                base = BASE * base % MOD

        return False
        
# leetcode submit region end(Prohibit modification and deletion)
