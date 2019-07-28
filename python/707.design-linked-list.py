'''
[707] Design Linked List

https://leetcode.com/problems/design-linked-list/description/

* algorithms
* Easy (21.55%)
* Source Code:       707.design-linked-list.py
* Total Accepted:    30.2K
* Total Submissions: 142.2K
* Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n[[],[1],[3],
[1,2],[1],[1],[1]]'

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next
 is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute
prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

        get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the
        new node will be the first node of the linked list.
        addAtTail(val) : Append a node of value val to the last element of the linked list.
        addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals 
        to the length of linked list, the node will be appended to the end of linked list. If index is greater than the
         length, the node will not be inserted. If index is negative, the node will be inserted at the head of the list.
        deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.


Example:


MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3


Note:


        All values will be in the range of [1, 1000].
        The number of operations will be in the range of [1, 1000].
        Please do not use the built-in LinkedList library.

'''


class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index > self.size - 1 or index < 0:
            return -1
        first = self.head
        for i in range(index):
            first = first.next
        return first.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.head = Node(val=val, next=self.head)
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        next = self.head
        if not next:
            return self.addAtHead(val=val)
        while next.next:
            next = next.next
        next.next = Node(val=val)
        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == self.size:
            return self.addAtTail(val)
        if index<=0:
            return self.addAtHead(val)
        if index > self.size:
            return
        first = self.head
        for i in range(index - 1):
            first = first.next
        first.next = Node(val=val, next=first.next)
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index<0 or index>=self.size:
            return
        if index==0:
            self.head=self.head.next
            return
        first = self.head
        for i in range(index - 1):
            first = first.next
        first.next = first.next.next
        if index == 0:
            self.head = first.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)f
# obj.deleteAtIndex(index)
