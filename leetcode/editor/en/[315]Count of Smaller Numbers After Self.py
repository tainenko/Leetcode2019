# Given an integer array nums, return an integer array counts where counts[i] 
# is the number of smaller elements to the right of nums[i]. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [-1,-1]
# Output: [0,0]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics Array Binary Search Divide and Conquer Binary Indexed Tree 
# Segment Tree Merge Sort Ordered Set 👍 8483 👎 227


# leetcode submit region begin(Prohibit modification and deletion)
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * (n + 1)

    def lowbit(self, x):
        return x & -x

    def update(self, x, v):
        while x <= self.n:
            self.arr[x] += v
            x += self.lowbit(x)

    def range(self, x):
        res = 0
        while x > 0:
            res += self.arr[x]
            x -= self.lowbit(x)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        alls = sorted(set(nums))
        m = {v: i for i, v in enumerate(alls, 1)}
        tree = BinaryIndexedTree(len(m))
        res = []
        for num in nums[::-1]:
            x = m[num]
            tree.update(x, 1)
            res.append(tree.range(x - 1))
        return res[::-1]
# leetcode submit region end(Prohibit modification and deletion)
