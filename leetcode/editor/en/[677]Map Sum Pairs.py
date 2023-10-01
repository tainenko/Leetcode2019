# Design a map that allows you to do the following: 
# 
#  
#  Maps a string key to a given value. 
#  Returns the sum of the values that have a key with a prefix equal to a given 
# string. 
#  
# 
#  Implement the MapSum class: 
# 
#  
#  MapSum() Initializes the MapSum object. 
#  void insert(String key, int val) Inserts the key-val pair into the map. If th
# e key already existed, the original key-value pair will be overridden to the new
#  one. 
#  int sum(string prefix) Returns the sum of all the pairs' value whose key star
# ts with the prefix. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MapSum", "insert", "sum", "insert", "sum"]
# [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
# Output
# [null, null, 3, null, 5]
# 
# Explanation
# MapSum mapSum = new MapSum();
# mapSum.insert("apple", 3);  
# mapSum.sum("ap");           // return 3 (apple = 3)
# mapSum.insert("app", 2);    
# mapSum.sum("ap");           // return 5 (apple + app = 3 + 2 = 5)
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= key.length, prefix.length <= 50 
#  key and prefix consist of only lowercase English letters. 
#  1 <= val <= 1000 
#  At most 50 calls will be made to insert and sum. 
#  
#  Related Topics Hash Table String Design Trie 
#  👍 985 👎 112
from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.v = 0

    def search(self, prefix):
        node = self
        for c in prefix:
            node = node.children[c]
        return node.v

    def update(self, key, val):
        node = self
        for c in key:
            node = node.children[c]
            node.v += val


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.m = defaultdict(int)

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        diff = val - self.m[key]
        self.m[key] = val
        self.trie.update(key, diff)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.trie.search(prefix)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# leetcode submit region end(Prohibit modification and deletion)
