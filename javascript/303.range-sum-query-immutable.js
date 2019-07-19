/**
 * [303] Range Sum Query - Immutable

https://leetcode.com/problems/range-sum-query-immutable/description/

* algorithms
* Easy (38.47%)
* Source Code:       303.range-sum-query-immutable.js
* Total Accepted:    144.5K
* Total Submissions: 373.6K
* Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3



Note:

You may assume that the array does not change.
There are many calls to sumRange function.

 */
/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    this.nums=nums;
    
};

/** 
 * @param {number} i 
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    let total=0;
    for(let idx=i;idx<=j;idx++){
        total+=this.nums[idx];
    }
    return total;
    
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(i,j)
 */
