class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


        In Pascal's triangle, each number is the sum of the two numbers directly above it.

        Example:


        Input: 5
        Output:
        [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]

        解題想法：
        Pascals triangle中第n列第i個元素，為前一例的i-1和i個元素之首，
        意即curr[i]=prev[i]+prev[i-1]。
        此外，第n列會比第n-1列多出一個[1]。
        [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1],
        [1,4,6,4,1]
        ]
        """
        if numRows<=0:
            return []
        res=[]
        curr=[1]
        for i in range(numRows):
            res.append(curr[:])
            prev=curr[:]
            for j in range(1,len(curr)):
                curr[j]=prev[j-1]+prev[j]
            curr.append(1)
        return res


