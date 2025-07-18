# Koko loves to eat bananas. There are n piles of bananas, the iᵗʰ pile has 
# piles[i] bananas. The guards have gone and will come back in h hours. 
# 
#  Koko can decide her bananas-per-hour eating speed of k. Each hour, she 
# chooses some pile of bananas and eats k bananas from that pile. If the pile has less 
# than k bananas, she eats all of them instead and will not eat any more bananas 
# during this hour. 
# 
#  Koko likes to eat slowly but still wants to finish eating all the bananas 
# before the guards return. 
# 
#  Return the minimum integer k such that she can eat all the bananas within h 
# hours. 
# 
#  
#  Example 1: 
# 
#  
# Input: piles = [3,6,7,11], h = 8
# Output: 4
#  
# 
#  Example 2: 
# 
#  
# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
#  
# 
#  Example 3: 
# 
#  
# Input: piles = [30,11,23,4,20], h = 6
# Output: 23
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= piles.length <= 10⁴ 
#  piles.length <= h <= 10⁹ 
#  1 <= piles[i] <= 10⁹ 
#  
# 
#  Related Topics Array Binary Search 👍 12448 👎 821


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def time(speed):
            return sum([(p - 1) // speed + 1 for p in piles])

        while low < high:
            mid = low + (high - low) // 2
            if time(mid) <= h:
                high = mid
            else:
                low = mid + 1
        return low
# leetcode submit region end(Prohibit modification and deletion)
