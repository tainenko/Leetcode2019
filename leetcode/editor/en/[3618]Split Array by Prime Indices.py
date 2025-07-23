# You are given an integer array nums. 
# 
#  Split nums into two arrays A and B using the following rule: 
# 
#  
#  Elements at prime indices in nums must go into array A. 
#  All other elements must go into array B. 
#  
# 
#  Return the absolute difference between the sums of the two arrays: |sum(A) - 
# sum(B)|. 
# 
#  Note: An empty array has a sum of 0. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [2,3,4] 
#  
# 
#  Output: 1 
# 
#  Explanation: 
# 
#  
#  The only prime index in the array is 2, so nums[2] = 4 is placed in array A. 
# 
#  The remaining elements, nums[0] = 2 and nums[1] = 3 are placed in array B. 
#  sum(A) = 4, sum(B) = 2 + 3 = 5. 
#  The absolute difference is |4 - 5| = 1. 
#  
# 
#  Example 2: 
# 
#  
#  Input: nums = [-1,5,7,0] 
#  
# 
#  Output: 3 
# 
#  Explanation: 
# 
#  
#  The prime indices in the array are 2 and 3, so nums[2] = 7 and nums[3] = 0 
# are placed in array A. 
#  The remaining elements, nums[0] = -1 and nums[1] = 5 are placed in array B. 
#  sum(A) = 7 + 0 = 7, sum(B) = -1 + 5 = 4. 
#  The absolute difference is |7 - 4| = 3. 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  Related Topics Array Math Number Theory 👍 31 👎 2


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitArray(self, nums: List[int]) -> int:
        arr1 = []
        arr2 = []
        for i, v in enumerate(nums):
            if self.is_prime(i):
                arr1.append(v)
            else:
                arr2.append(v)
        return abs(sum(arr1) - sum(arr2))

    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
