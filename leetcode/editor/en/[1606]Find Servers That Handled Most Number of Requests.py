# You have k servers numbered from 0 to k-1 that are being used to handle 
# multiple requests simultaneously. Each server has infinite computational capacity but 
# cannot handle more than one request at a time. The requests are assigned to 
# servers according to a specific algorithm: 
# 
#  
#  The iᵗʰ (0-indexed) request arrives. 
#  If all servers are busy, the request is dropped (not handled at all). 
#  If the (i % k)ᵗʰ server is available, assign the request to that server. 
#  Otherwise, assign the request to the next available server (wrapping around 
# the list of servers and starting from 0 if necessary). For example, if the iᵗʰ 
# server is busy, try to assign the request to the (i+1)ᵗʰ server, then the (i+2)ᵗʰ 
# server, and so on. 
#  
# 
#  You are given a strictly increasing array arrival of positive integers, 
# where arrival[i] represents the arrival time of the iᵗʰ request, and another array 
# load, where load[i] represents the load of the iᵗʰ request (the time it takes to 
# complete). Your goal is to find the busiest server(s). A server is considered 
# busiest if it handled the most number of requests successfully among all the 
# servers. 
# 
#  Return a list containing the IDs (0-indexed) of the busiest server(s). You 
# may return the IDs in any order. 
# 
#  
#  Example 1: 
#  
#  
# Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
# Output: [1] 
# Explanation: 
# All of the servers start out available.
# The first 3 requests are handled by the first 3 servers in order.
# Request 3 comes in. Server 0 is busy, so it's assigned to the next available 
# server, which is 1.
# Request 4 comes in. It cannot be handled since all servers are busy, so it is 
# dropped.
# Servers 0 and 2 handled one request each, while server 1 handled two requests.
#  Hence server 1 is the busiest server.
#  
# 
#  Example 2: 
# 
#  
# Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
# Output: [0]
# Explanation: 
# The first 3 requests are handled by first 3 servers.
# Request 3 comes in. It is handled by server 0 since the server is available.
# Server 0 handled two requests, while servers 1 and 2 handled one request each.
#  Hence server 0 is the busiest server.
#  
# 
#  Example 3: 
# 
#  
# Input: k = 3, arrival = [1,2,3], load = [10,12,11]
# Output: [0,1,2]
# Explanation: Each server handles a single request, so they are all considered 
# the busiest.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= 10⁵ 
#  1 <= arrival.length, load.length <= 10⁵ 
#  arrival.length == load.length 
#  1 <= arrival[i], load[i] <= 10⁹ 
#  arrival is strictly increasing. 
#  
# 
#  Related Topics Array Greedy Heap (Priority Queue) Ordered Set 👍 556 👎 24
import heapq

# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedList


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        free = SortedList(range(k))
        busy = []
        cnt = Counter()
        mx = 0
        for i, (start, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start:
                free.add(busy[0][1])
                heapq.heappop(busy)
            if not free:
                continue
            j = free.bisect_left(i % k)
            if j == len(free):
                j = 0
            server = free[j]
            cnt[server] += 1
            mx = max(cnt[server], mx)
            free.remove(server)
            heapq.heappush(busy, (start + duration, server))
        return [i for i in range(k) if cnt[i] == mx]

# leetcode submit region end(Prohibit modification and deletion)
