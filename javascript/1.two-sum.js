/**
    [1] Two Sum

    https://leetcode.com/problems/two-sum/description/

    * algorithms
    * Easy (40.17%)
    * Source Code:       1.two-sum.js
    * Total Accepted:    1.4M
    * Total Submissions: 3.5M
    * Testcase Example:  '[2,7,11,15]\n9'

    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:


    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    //HashTable，時間複雜度O(n)，空間複雜度O(n)
    var myMap = new Map();
    for(let i=0;i<nums.length;i++){
        if(myMap.has(nums[i])){
            return [i,myMap.get(nums[i])]
        }else{
            myMap.set(target-nums[i],i);
        }
    }
    
};

var solution2 = function(nums,target){
    //暴力破解，時間雜複度O(n^2)，空間複雜度O(1)
    //相當於用兩層for loop
    return nums.reduce((results,value,index)=>{
        for(let i =index+1;i<length;i++) {
            if (nums[i] + value === target) {
                results = [index, i];
            }
        }
    },[])
};

var solution3 = function(nums,target){
    //先排序再求解
    //時間複雜度O(nlogn)，空間複雜度O(n)
    //效能主要花在排序
    let cloneData = nums.map((index, item) => {
        return {
            val: index,
            index: item,
        };
    });
  //step1.sort
  //time complexity:O(nlogn)
  //space complexity: O(1)
    cloneData.sort((a, b) => a.val - b.val);
  //step2.loop
  //time complexity=:O(n)
    let i = 0, j = cloneData.length - 1;
    let sum;
    while ((sum = cloneData[i].val + cloneData[j].val) != target) {
        sum > target ? j-- : i++;
    }
    i = cloneData[i].index;
    j = cloneData[j].index;
    return i < j ? [i, j] : [j, i];

};