'''
[1046] Last Stone Weight

https://leetcode.com/problems/last-stone-weight/description/

* algorithms
* Easy (63.25%)
* Source Code:       1046.last-stone-weight.py
* Total Accepted:    9.7K
* Total Submissions: 15.5K
* Testcase Example:  '[2,7,4,1,8,1]'

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:


        If x == y, both stones are totally destroyed;
        If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.


At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:


Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

 

Note:


        1 <= stones.length <= 30
        1 <= stones[i] <= 1000

'''
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        _sorted=sorted(stones)
        while len(_sorted)>1:
            x=_sorted.pop()
            y=_sorted.pop()
            if x==y:
                continue
            else:
                tmp=x-y
                _sorted=self.insert_to_sorted(tmp,_sorted)
        if _sorted:
            return _sorted[0]
        else:
            return 0

    def insert_to_sorted(self,n,lst):
        index=len(lst)
        for i in range(len(lst)):
            if lst[i] > n:
                index = i
                break
            # Inserting n in the list
        lst = lst[:index] + [n] + lst[index:]
        return lst

