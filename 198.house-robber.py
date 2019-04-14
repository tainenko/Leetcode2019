class Solution(object):
    def rob(self, nums):
        """
        [198] House Robber

        https://leetcode.com/problems/house-robber/description/

        * algorithms
        * Easy (40.88%)
        * Source Code:       198.house-robber.py
        * Total Accepted:    306.4K
        * Total Submissions: 749.3K
        * Testcase Example:  '[1,2,3,1]'

        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

        Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

        Example 1:


        Input: [1,2,3,1]
        Output: 4
        Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                     Total amount you can rob = 1 + 3 = 4.

        Example 2:


        Input: [2,7,9,3,1]
        Output: 12
        Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
                     Total amount you can rob = 2 + 9 + 1 = 12.

        :type nums: List[int]
        :rtype: int
        """
        '''
        解題思題：
        題目要求不能到相鄰的屋子。假如果有一家，那就只能偷一家，假如有兩家，就選最大的一家偷，
        假如有n家，有兩個選擇，一是偷第n家，累計的金額是第n家+偷到第n-2家的總和，第二種是不偷第n家
        累計的金額同偷到第n-2家的總和。
        '''
        curr = prev = 0
        for num in nums:
            prev, curr = curr, max(num + prev, curr)
        return curr

    def rob2(self, nums):
        if len(nums)<=1:
            return 0
        if len(nums)==2:
            return max(nums[0],nums[1])
        money=[0]*len(nums)
        money[0],money[1]=nums[0],max(nums[0],nums[1])

        for i in range(2,len(nums)):
            money[i]=max(nums[i]+money[i-2],money[i-1])
        return money[-1]

        
