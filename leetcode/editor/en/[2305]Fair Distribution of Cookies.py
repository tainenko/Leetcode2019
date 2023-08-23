# You are given an integer array cookies, where cookies[i] denotes the number 
# of cookies in the iᵗʰ bag. You are also given an integer k that denotes the 
# number of children to distribute all the bags of cookies to. All the cookies in the 
# same bag must go to the same child and cannot be split up. 
# 
#  The unfairness of a distribution is defined as the maximum total cookies 
# obtained by a single child in the distribution. 
# 
#  Return the minimum unfairness of all distributions. 
# 
#  
#  Example 1: 
# 
#  
# Input: cookies = [8,15,10,20,8], k = 2
# Output: 31
# Explanation: One optimal distribution is [8,15,8] and [10,20]
# - The 1ˢᵗ child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 
# cookies.
# - The 2ⁿᵈ child receives [10,20] which has a total of 10 + 20 = 30 cookies.
# The unfairness of the distribution is max(31,30) = 31.
# It can be shown that there is no distribution with an unfairness less than 31.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: cookies = [6,1,3,2,2,4,1,2], k = 3
# Output: 7
# Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
# - The 1ˢᵗ child receives [6,1] which has a total of 6 + 1 = 7 cookies.
# - The 2ⁿᵈ child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
# - The 3ʳᵈ child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
# The unfairness of the distribution is max(7,7,7) = 7.
# It can be shown that there is no distribution with an unfairness less than 7.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= cookies.length <= 8 
#  1 <= cookies[i] <= 10⁵ 
#  2 <= k <= cookies.length 
#  
# 
#  Related Topics Array Dynamic Programming Backtracking Bit Manipulation 
# Bitmask 👍 2310 👎 93
from math import inf


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def dfs(i):
            nonlocal res
            if i >= len(cookies):
                res = max(cnt)
                return
            for j in range(k):
                if cnt[j] + cookies[i] >= res or (j and cnt[j] == cnt[j - 1]):
                    continue
                cnt[j] += cookies[i]
                dfs(i + 1)
                cnt[j] -= cookies[i]

        cnt = [0] * k
        cookies.sort(reverse=True)
        res = inf
        dfs(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)
