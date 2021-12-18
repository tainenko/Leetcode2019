# Design a data structure that accepts a stream of integers and checks if it 
# has a pair of integers that sum up to a particular value. 
# 
#  Implement the TwoSum class: 
# 
#  
#  TwoSum() Initializes the TwoSum object, with an empty array initially. 
#  void add(int number) Adds number to the data structure. 
#  boolean find(int value) Returns true if there exists any pair of numbers 
# whose sum is equal to value, otherwise, it returns false. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["TwoSum", "add", "add", "add", "find", "find"]
# [[], [1], [3], [5], [4], [7]]
# Output
# [null, null, null, null, true, false]
# 
# Explanation
# TwoSum twoSum = new TwoSum();
# twoSum.add(1);   // [] --> [1]
# twoSum.add(3);   // [1] --> [1,3]
# twoSum.add(5);   // [1,3] --> [1,3,5]
# twoSum.find(4);  // 1 + 3 = 4, return true
# twoSum.find(7);  // No two integers sum up to 7, return false
#  
# 
#  
#  Constraints: 
# 
#  
#  -10⁵ <= number <= 10⁵ 
#  -2³¹ <= value <= 2³¹ - 1 
#  At most 10⁴ calls will be made to add and find. 
#  
#  Related Topics Array Hash Table Two Pointers Design Data Stream 👍 478 👎 350
# 


# leetcode submit region begin(Prohibit modification and deletion)
class TwoSum:

    def __init__(self):
        self.nums = []
        self.map = {}

    def add(self, number: int) -> None:
        for num in self.nums:
            self.map[number + num] = True
        self.nums.append(number)

    def find(self, value: int) -> bool:
        return self.map.get(value, False)

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# leetcode submit region end(Prohibit modification and deletion)
