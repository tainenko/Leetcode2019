# You are given two integers height and width representing a garden of size 
# height x width. You are also given: 
# 
#  
#  an array tree where tree = [treer, treec] is the position of the tree in the 
# garden, 
#  an array squirrel where squirrel = [squirrelr, squirrelc] is the position of 
# the squirrel in the garden, 
#  and an array nuts where nuts[i] = [nutir, nutic] is the position of the iᵗʰ 
# nut in the garden. 
#  
# 
#  The squirrel can only take at most one nut at one time and can move in four 
# directions: up, down, left, and right, to the adjacent cell. 
# 
#  Return the minimal distance for the squirrel to collect all the nuts and put 
# them under the tree one by one. 
# 
#  The distance is the number of moves. 
# 
#  
#  Example 1: 
#  
#  
# Input: height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [
# 2,5]]
# Output: 12
# Explanation: The squirrel should go to the nut at [2, 5] first to achieve a 
# minimal distance.
#  
# 
#  Example 2: 
#  
#  
# Input: height = 1, width = 3, tree = [0,1], squirrel = [0,0], nuts = [[0,2]]
# Output: 3
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= height, width <= 100 
#  tree.length == 2 
#  squirrel.length == 2 
#  1 <= nuts.length <= 5000 
#  nuts[i].length == 2 
#  0 <= treer, squirrelr, nutir <= height 
#  0 <= treec, squirrelc, nutic <= width 
#  
# 
#  Related Topics Array Math 👍 336 👎 36
from math import inf


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        s = sum([dist(tree, nut) for nut in nuts])
        res = inf
        for nut in nuts:
            res = min(res, s * 2 + dist(squirrel, nut) - dist(tree, nut))
        return res

    # leetcode submit region end(Prohibit modification and deletion)
