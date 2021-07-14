# Given a non-empty list of words, return the k most frequent elements. 
#  Your answer should be sorted by frequency from highest to lowest. If two word
# s have the same frequency, then the word with the lower alphabetical order comes
#  first. 
# 
#  Example 1: 
#  
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
#  
#  
# 
#  Example 2: 
#  
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
# , k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
#  
#  
# 
#  Note: 
#  
#  You may assume k is always valid, 1 ≤ k ≤ number of unique elements. 
#  Input words contain only lowercase letters. 
#  
#  
# 
#  Follow up: 
#  
#  Try to solve it in O(n log k) time and O(n) extra space. 
#  
#  Related Topics Hash Table String Trie Sorting Heap (Priority Queue) Bucket So
# rt Counting 
#  👍 3273 👎 212


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        return [item[0] for item in sorted([(key, val) for key, val in count.items()], key=lambda x: (-x[1], x[0]))][:k]
    # leetcode submit region end(Prohibit modification and deletion)
