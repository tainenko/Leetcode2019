# Two strings, X and Y, are considered similar if either they are identical or 
# we can make them equivalent by swapping at most two letters (in distinct 
# positions) within the string X. 
# 
#  For example, "tars" and "rats" are similar (swapping at positions 0 and 2), 
# and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", 
# or "arts". 
# 
#  Together, these form two connected groups by similarity: {"tars", "rats", 
# "arts"} and {"star"}. Notice that "tars" and "arts" are in the same group even 
# though they are not similar. Formally, each group is such that a word is in the 
# group if and only if it is similar to at least one other word in the group. 
# 
#  We are given a list strs of strings where every string in strs is an anagram 
# of every other string in strs. How many groups are there? 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["tars","rats","arts","star"]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["omv","ovm"]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 300 
#  1 <= strs[i].length <= 300 
#  strs[i] consists of lowercase letters only. 
#  All words in strs have the same length and are anagrams of each other. 
#  
# 
#  Related Topics Array Hash Table String Depth-First Search Breadth-First 
# Search Union Find 👍 2247 👎 213


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        p = [i for i in range(len(strs))]
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if sum([strs[i][k] != strs[j][k] for k in range(len(strs[i]))]) <= 2:
                    p[find(i)] = find(j)

        return sum([i == find(i) for i in range(len(strs))])

# leetcode submit region end(Prohibit modification and deletion)
