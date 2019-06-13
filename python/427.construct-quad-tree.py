'''
[427] Construct Quad Tree

https://leetcode.com/problems/construct-quad-tree/description/

* algorithms
* Easy (56.69%)
* Source Code:       427.construct-quad-tree.py
* Total Accepted:    11.7K
* Total Submissions: 20.5K
* Testcase Example:  '[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]'

We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.

Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.

Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:

Given the 8 x 8 grid below, we want to construct the corresponding quad tree:



It can be divided according to the definition above:



 

The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is represented as *.



Note:


        N is less than 1000 and guaranteened to be a power of 2.
        If you want to know more about the quad tree, you can refer to its wiki.

'''
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        length=len(grid)
        node = Node()
        if self.checkgrid(grid):
            node.isLeaf=True
            node.val=grid[0][0]
        else:
            node.isLeaf=False
            node.val='*'
            half=length//2
            tleft=[grid[i][:half] for i in range(half)]
            tright=[grid[i][half:] for i in range(half)]
            bleft=[grid[i][:half] for i in range(half,length)]
            bright=[grid[i][half:] for i in range(half,length)]
            node.topLeft=self.construct(tleft)
            node.topRight=self.construct(tright)
            node.bottomLeft=self.construct(bleft)
            node.bottomRight=self.construct(bright)
        return node
    def checkgrid(self,grid):
        length=len(grid)
        for i in range(length):
            for j in range(length):
                if grid[i][j]!=grid[0][0]:
                    return False
        return True



        
