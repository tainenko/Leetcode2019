# You are given an integer array nums that is sorted in non-decreasing order. 
# 
#  Determine if it is possible to split nums into one or more subsequences such 
# that both of the following conditions are true: 
# 
#  
#  Each subsequence is a consecutive increasing sequence (i.e. each integer is e
# xactly one more than the previous integer). 
#  All subsequences have a length of 3 or more. 
#  
# 
#  Return true if you can split nums according to the above conditions, or false
#  otherwise. 
# 
#  A subsequence of an array is a new array that is formed from the original arr
# ay by deleting some (can be none) of the elements without disturbing the relativ
# e positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3
# ,4,5] while [1,3,2] is not). 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3,3,4,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,5] --> 1, 2, 3
# [1,2,3,3,4,5] --> 3, 4, 5
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,3,4,4,5,5]
# Output: true
# Explanation: nums can be split into the following subsequences:
# [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
# [1,2,3,3,4,4,5,5] --> 3, 4, 5
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [1,2,3,4,4,5]
# Output: false
# Explanation: It is impossible to split nums into consecutive increasing subseq
# uences of length 3 or more.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -1000 <= nums[i] <= 1000 
#  nums is sorted in non-decreasing order. 
#  
#  Related Topics Array Hash Table Greedy Heap (Priority Queue) 
#  👍 1725 👎 500


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter, defaultdict


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = Counter(nums)
        needs = defaultdict(int)
        for num in nums:
            if counter[num] == 0:
                continue
            elif needs[num] > 0:
                needs[num] -= 1
                needs[num + 1] += 1
            elif counter[num + 1] > 0 and counter[num + 2] > 0:
                counter[num + 1] -= 1
                counter[num + 2] -= 1
                needs[num + 3] += 1
            else:
                return False
            counter[num] -= 1
        return True

# leetcode submit region end(Prohibit modification and deletion)
