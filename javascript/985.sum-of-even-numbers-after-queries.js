/**
 * [985] Sum of Even Numbers After Queries

    https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

    * algorithms
    * Easy (65.93%)
    * Source Code:       985.sum-of-even-numbers-after-queries.js
    * Total Accepted:    16K
    * Total Submissions: 24.6K
    * Testcase Example:  '[1,2,3,4]\n[[1,0],[-3,1],[-4,0],[2,3]]'

    We have an array A of integers, and an array queries of queries.

    For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

    (Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

    Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

     

    Example 1:


    Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
    Output: [8,6,2,4]
    Explanation:
    At the beginning, the array is [1,2,3,4].
    After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
    After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
    After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
    After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.


     

    Note:


            1 <= A.length <= 10000
            -10000 <= A[i] <= 10000
            1 <= queries.length <= 10000
            -10000 <= queries[i][0] <= 10000
            0 <= queries[i][1] < A.length
 * @param {number[]} A
 * @param {number[][]} queries
 * @return {number[]}
 */
var sumEvenAfterQueries = function(A, queries) {
    //解題思路
    //先求出所有A中偶數之和
    //再traverse queries，若A中異動的元素為偶數則從總和中減去，若元素異動和為偶數則加到總和中。
    //計算完後將結果加到res的array裡題。
    var total=A.reduce((acc, value) => value%2 == 0 ? acc + value : acc,0);
    return queries.map((q)=>{
        if(A[q[1]]%2===0){
            total-=A[q[1]];
        }
        A[q[1]]+=q[0];
        if(A[q[1]]%2==0){
            total+=A[q[1]];
        }
        return total;
    });
    
};
