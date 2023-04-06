# You are given m arrays, where each array is sorted in ascending order. 
# 
#  You can pick up two integers from two different arrays (each array picks one)
#  and calculate the distance. We define the distance between two integers a and 
# b to be their absolute difference |a - b|. 
# 
#  Return the maximum distance. 
# 
#  
#  Example 1: 
# 
#  
# Input: arrays = [[1,2,3],[4,5],[1,2,3]]
# Output: 4
# Explanation: One way to reach the maximum distance 4 is to pick 1 in the 
# first or third array and pick 5 in the second array.
#  
# 
#  Example 2: 
# 
#  
# Input: arrays = [[1],[1]]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  m == arrays.length 
#  2 <= m <= 10⁵ 
#  1 <= arrays[i].length <= 500 
#  -10⁴ <= arrays[i][j] <= 10⁴ 
#  arrays[i] is sorted in ascending order. 
#  There will be at most 10⁵ integers in all the arrays. 
#  
# 
#  Related Topics Array Greedy 👍 618 👎 62


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        largest = (0, -2147483647)
        second_largest = (0, -2147483647)
        for i, arr in enumerate(arrays):
            if arr[-1] > largest[1]:
                second_largest = largest
                largest = (i, arr[-1])
            elif arr[-1] > second_largest[1]:
                second_largest = (i, arr[-1])

        smallest = (0, 2147483647)
        second_smallest = (0, 2147483647)
        for i, arr in enumerate(arrays):
            if arr[0] < smallest[1]:
                second_smallest = smallest
                smallest = (i, arr[0])
            elif arr[0] < second_smallest[1]:
                second_smallest = (i, arr[0])

        if smallest[0] != largest[0]:
            return abs(smallest[1] - largest[1])

        return max(abs(smallest[1] - second_largest[1]), abs(largest[1] - second_smallest[1]))
# leetcode submit region end(Prohibit modification and deletion)
