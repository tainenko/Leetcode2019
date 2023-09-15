# A string s is called happy if it satisfies the following conditions: 
# 
#  
#  s only contains the letters 'a', 'b', and 'c'. 
#  s does not contain any of "aaa", "bbb", or "ccc" as a substring. 
#  s contains at most a occurrences of the letter 'a'. 
#  s contains at most b occurrences of the letter 'b'. 
#  s contains at most c occurrences of the letter 'c'. 
#  
# 
#  Given three integers a, b, and c, return the longest possible happy string. 
# If there are multiple longest happy strings, return any of them. If there is no 
# such string, return the empty string "". 
# 
#  A substring is a contiguous sequence of characters within a string. 
# 
#  
#  Example 1: 
# 
#  
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
#  
# 
#  Example 2: 
# 
#  
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= a, b, c <= 100 
#  a + b + c > 0 
#  
# 
#  Related Topics String Greedy Heap (Priority Queue) 👍 1881 👎 235


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        res = ""
        while heap:
            cnt1, c1 = heapq.heappop(heap)
            if len(res) >= 2 and c1 == res[-1] == res[-2]:
                if not heap:
                    break
                cnt2, c2 = heapq.heappop(heap)
                res += c2
                cnt2 += 1
                if cnt2 < 0:
                    heapq.heappush(heap, (cnt2, c2))
            res += c1
            cnt1 += 1
            if cnt1 < 0:
                heapq.heappush(heap, (cnt1, c1))
        return res
        # leetcode submit region end(Prohibit modification and deletion)
