'''
[703] Kth Largest Element in a Stream

https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

* algorithms
* Easy (46.59%)
* Source Code:       703.kth-largest-element-in-a-stream.py
* Total Accepted:    38.1K
* Total Submissions: 81.4K
* Testcase Example:  '["KthLargest","add","add","add","add","add"]\n[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'

Design a class to find the kth largest element in a stream. Note that it is the kth largest element
in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream. For each call to the method KthLargest.add, return
the element representing the kth largest element in the stream.

Example:


int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8


Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.

'''
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums=nums
        self.size=len(nums)
        self.k=k
        heapq.heapify(self.nums)
        while self.size>k:
            heapq.heappop(self.nums)
            self.size-=1
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size<self.k:
            heapq.heappush(self.nums,val)
            self.size+=1
        elif val >self.nums[0]:
            heapq.heapreplace(self.nums,val)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
