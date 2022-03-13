# Given an array arr of positive integers sorted in a strictly increasing order,
#  and an integer k.
#
#  Find the kᵗʰ positive integer that is missing from this array.
#
#
#  Example 1:
#
#
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5
# ᵗʰ missing positive integer is 9.
#
#
#  Example 2:
#
#
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2ⁿᵈ missing
# positive integer is 6.
#
#
#
#  Constraints:
#
#
#  1 <= arr.length <= 1000
#  1 <= arr[i] <= 1000
#  1 <= k <= 1000
#  arr[i] < arr[j] for 1 <= i < j <= arr.length
#
#  Related Topics Array Binary Search 👍 2162 👎 160


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if len(arr) == arr[-1]:
            return arr[-1] + k
        candidate = 1
        cnt = 0
        for num in arr:
            if candidate == num:
                candidate += 1
                continue
            else:
                cnt += num - candidate
                if cnt >= k:
                    return num - cnt + k-1
                candidate = num + 1
        return candidate + k - cnt-1

# leetcode submit region end(Prohibit modification and deletion)
