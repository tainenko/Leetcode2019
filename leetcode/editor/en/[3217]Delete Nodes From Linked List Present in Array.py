# You are given an array of integers nums and the head of a linked list. Return 
# the head of the modified linked list after removing all nodes from the linked 
# list that have a value that exists in nums. 
# 
#  
#  Example 1: 
# 
#  
#  Input: nums = [1,2,3], head = [1,2,3,4,5] 
#  
# 
#  Output: [4,5] 
# 
#  Explanation: 
# 
#  
# 
#  Remove the nodes with values 1, 2, and 3. 
# 
#  Example 2: 
# 
#  
#  Input: nums = [1], head = [1,2,1,2,1,2] 
#  
# 
#  Output: [2,2,2] 
# 
#  Explanation: 
# 
#  
# 
#  Remove the nodes with value 1. 
# 
#  Example 3: 
# 
#  
#  Input: nums = [5], head = [1,2,3,4] 
#  
# 
#  Output: [1,2,3,4] 
# 
#  Explanation: 
# 
#  
# 
#  No node has value 5. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁵ 
#  All elements in nums are unique. 
#  The number of nodes in the given list is in the range [1, 10⁵]. 
#  1 <= Node.val <= 10⁵ 
#  The input is generated such that there is at least one node in the linked 
# list that has a value not present in nums. 
#  
# 
#  Related Topics Array Hash Table Linked List 👍 667 👎 31


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not nums:
            return head
        nums = set(nums)
        head = ListNode(next=head)
        node = head
        while node.next:
            if node.next.val in nums:
                node.next = node.next.next
                continue
            node = node.next
        return head.next
# leetcode submit region end(Prohibit modification and deletion)
