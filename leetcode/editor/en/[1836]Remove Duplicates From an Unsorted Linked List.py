# Given the head of a linked list, find all the values that appear more than 
# once in the list and delete the nodes that have any of those values. 
# 
#  Return the linked list after the deletions. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,2]
# Output: [1,3]
# Explanation: 2 appears twice in the linked list, so all 2's should be deleted.
#  After deleting all 2's, we are left with [1,3].
#  
# 
#  Example 2: 
#  
#  
# Input: head = [2,1,1,2]
# Output: []
# Explanation: 2 and 1 both appear twice. All the elements should be deleted.
#  
# 
#  Example 3: 
#  
#  
# Input: head = [3,2,2,1,3,2,4]
# Output: [1,4]
# Explanation: 3 appears twice and 2 appears three times. After deleting all 3
# 's and 2's, we are left with [1,4].
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 10⁵] 
#  1 <= Node.val <= 10⁵ 
#  
# 
#  Related Topics Hash Table Linked List 👍 348 👎 11


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        cnt = Counter()
        node = head
        while node:
            cnt[node.val] += 1
            node = node.next

        dummy = ListNode(0, head)
        pre, curr = dummy, head
        while curr:
            if cnt[curr.val] > 1:
                pre.next = curr.next
            else:
                pre = curr
            curr = curr.next

        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
