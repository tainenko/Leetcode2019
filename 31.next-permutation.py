'''
[31] Next Permutation

https://leetcode.com/problems/next-permutation/description/

* algorithms
* Medium (30.57%)
* Source Code:       31.next-permutation.py
* Total Accepted:    244.8K
* Total Submissions: 799.6K
* Testcase Example:  '[1,2,3]'

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
