/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} node
 * @return {void} Do not return anything, modify node in-place instead.
 */
/**
 * [237] Delete Node in a Linked List

https://leetcode.com/problems/delete-node-in-a-linked-list/description/

* algorithms
* Easy (52.63%)
* Source Code:       237.delete-node-in-a-linked-list.0.py
* Total Accepted:    275.8K
* Total Submissions: 522.3K
* Testcase Example:  '[4,5,1,9]\n5'

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:


Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.


Example 2:


Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


 

Note:


        The linked list will have at least two elements.
        All of the nodes' values will be unique.
        The given node will not be the tail and it will always be a valid node of the linked list.
        Do not return anything from your function.

 */
var deleteNode = function(node) {
    // 解題思路
    // 題目已給定欲刪除的node，所以不用再遍歷linked list
    // 我們想要把當前節點刪掉，有兩個方法
    // 第一、將前一個節點的next指向欲刪除的節點後面的那一個，再將當前節點刪除
    // 第二、將欲刪除的節點val覆蓋成下一節點的val，然後把下一節點刪除。
    let tmp=node;
    node.val=node.next.val;
    node.next=node.next.next;
    delete tmp;
};
