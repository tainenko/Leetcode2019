/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
/**
 * [2] Add Two Numbers

https://leetcode.com/problems/add-two-numbers/description/

* algorithms
* Medium (30.38%)
* Source Code:       2.add-two-numbers.js
* Total Accepted:    741.3K
* Total Submissions: 2.4M
* Testcase Example:  '[2,4,3]\n[5,6,4]'

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:


Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

 */
var addTwoNumbers = function(l1, l2) {
    let head=node=new ListNode(0);
    let sum=carry=0;
    while(l1||l2||sum){
        if(l1){
            sum+=l1.val;
            l1=l1.next;
        };
        if(l2){
            sum+=l2.val;
            l2=l2.next;
        }
        if(sum>=10){
            carry=1;
            sum-=10;
        }
        node.next=new ListNode(sum);
        node=node.next;
        sum=carry;
        carry=0;
    }
    return head.next;
};
