# You are given an array people where people[i] is the weight of the iᵗʰ person,
#  and an infinite number of boats where each boat can carry a maximum weight of 
# limit. Each boat carries at most two people at the same time, provided the sum 
# of the weight of those people is at most limit. 
# 
#  Return the minimum number of boats to carry every given person. 
# 
#  
#  Example 1: 
# 
#  
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
#  
# 
#  Example 2: 
# 
#  
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
#  
# 
#  Example 3: 
# 
#  
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= people.length <= 5 * 10⁴ 
#  1 <= people[i] <= limit <= 3 * 10⁴ 
#  
# 
#  Related Topics Array Two Pointers Greedy Sorting 👍 3796 👎 101


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
            res += 1
        return res

    # leetcode submit region end(Prohibit modification and deletion)
