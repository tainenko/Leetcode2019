# You are given an array of strings names, and an array heights that consists 
# of distinct positive integers. Both arrays are of length n. 
# 
#  For each index i, names[i] and heights[i] denote the name and height of the 
# iᵗʰ person. 
# 
#  Return names sorted in descending order by the people's heights. 
# 
#  
#  Example 1: 
# 
#  
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
#  
# 
#  Example 2: 
# 
#  
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second 
# Bob.
#  
# 
#  
#  Constraints: 
# 
#  
#  n == names.length == heights.length 
#  1 <= n <= 10³ 
#  1 <= names[i].length <= 20 
#  1 <= heights[i] <= 10⁵ 
#  names[i] consists of lower and upper case English letters. 
#  All the values of heights are distinct. 
#  
# 
#  Related Topics Array Hash Table String Sorting 👍 344 👎 3


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        people.sort(key=lambda x: -x[1])
        return [name for name, _ in people]
# leetcode submit region end(Prohibit modification and deletion)
