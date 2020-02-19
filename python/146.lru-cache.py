#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (26.69%)
# Total Accepted:    344.3K
# Total Submissions: 1.3M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#
class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.__capacity = capacity
        self.__size = 0
        self.__dict = {}
        self.__root = ListNode(0, 0)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.__dict:
            return -1
        node = self.__dict[key]
        self.__del_node_from_list(node)
        self.__add_node_at_head(node)
        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.__dict:
            node = self.__dict[key]
            self.__del_node_from_list(node)
            self.__add_node_at_head(node)
            node.value = value
            return
        if self.__size >= self.__capacity:
            self.__del_node_from_tail()
            self.__size -= 1
        node = ListNode(key, value)
        self.__dict[key] = node
        self.__add_node_at_head(node)
        self.__size += 1

    def __add_node_at_head(self, node):
        next = self.__root.next
        node.next = next
        node.prev = self.__root
        self.__root.next = node
        next.prev = node

    def __del_node_from_list(self, node):
        if node == self.__root:
            return
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = node.next = None

    def __del_node_from_tail(self):
        if self.__size == 0:
            return
        node = self.__root.prev
        del self.__dict[node.key]
        self.__del_node_from_list(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
