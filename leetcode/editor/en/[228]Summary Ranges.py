# You are given a sorted unique integer array nums. 
# 
#  Return the smallest sorted list of ranges that cover all the numbers in the 
# array exactly. That is, each element of nums is covered by exactly one of the 
# ranges, and there is no integer x such that x is in one of the ranges but not in 
# nums. 
# 
#  Each range [a,b] in the list should be output as: 
# 
#  
#  "a->b" if a != b 
#  "a" if a == b 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 20 
#  -2³¹ <= nums[i] <= 2³¹ - 1 
#  All the values of nums are unique. 
#  nums is sorted in ascending order. 
#  
#  Related Topics Array 👍 1784 👎 1012


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        tmp = []
        for num in nums:
            if not tmp:
                tmp.append(num)
                continue
            else:
                if num == tmp[-1] + 1:
                    tmp.append(num)
                else:
                    res.append(tmp)
                    tmp = [num]
        res.append(tmp)
        for i in range(len(res)):
            if len(res[i]) == 1:
                res[i] = str(res[i][0])
                continue
            res[i] = f"{res[i][0]}->{res[i][-1]}"
        return res

# leetcode submit region end(Prohibit modification and deletion)
