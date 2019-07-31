#
# @lc app=leetcode id=447 lang=python
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (50.23%)
# Total Accepted:    56.8K
# Total Submissions: 113K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
#
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
#
# Example:
#
#
# Input:
# [[0,0],[1,0],[2,0]]
#
# Output:
# 2
#
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
#
#
#
#
#
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def get_dist(p1,p2):
            return (p2[0]-p1[0])**2+(p2[1]-p1[1])**2

        def find_Boomerangs(points):
            point1=points[0]
            dists=dict()
            for i in range(1,len(points)):
                dist=get_dist(point1,points[i])
                dists[dist]=dists.get(dist,0)+1
            return sum([x*(x-1) for x in dists.values()])

        count=0
        for i in range(len(points)):
            points[0],points[i]=points[i],points[0]
            count+=find_Boomerangs(points)
            points[0], points[i] = points[i], points[0]
        return count


