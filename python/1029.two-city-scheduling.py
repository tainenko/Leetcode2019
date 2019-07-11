'''
[1029] Two City Scheduling

https://leetcode.com/problems/two-city-scheduling/description/

* algorithms
* Easy (54.10%)
* Source Code:       1029.two-city-scheduling.py
* Total Accepted:    10.5K
* Total Submissions: 19.4K
* Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:


Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.


 

Note:


        1 <= costs.length <= 100
        It is guaranteed that costs.length is even.
        1 <= costs[i][0], costs[i][1] <= 1000
'''
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        A = sorted(costs,key = lambda x : x[0]-x[1])
        return sum([x[0] for x in A[:(len(A)//2)]])+sum([y[1] for y in A[len(A)//2:]])
        
