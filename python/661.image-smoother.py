#
# @lc app=leetcode id=661 lang=python
#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (49.16%)
# Total Accepted:    37.3K
# Total Submissions: 75.9K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D integer matrix M representing the gray scale of an image, you need
# to design a smoother to make the gray scale of each cell becomes the average
# gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
# cell has less than 8 surrounding cells, then use as many as you can.
# 
# Example 1:
# 
# Input:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# Output:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# 
# 
# 
# Note:
# 
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
# 
# 
#
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        解題思路：
        暴力解，計算九宮格的平均值。
        計算和時需要判斷index是否合法。
        '''
        w=len(M)
        h=len(M[0])
        res=[[None]*h for _ in range(w)]
        for i in range(w):
            for j in range(h):
                count=0
                _sum=0
                for l in range(-1,2):
                    for k in range(-1,2):
                        if 0<=i+l<w and 0<=j+k<h:
                            count+=1
                            _sum+=M[i+l][j+k]
                res[i][j]=_sum//count
        return res