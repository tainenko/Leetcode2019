# You are given a string num, representing a large integer, and an integer k. 
# 
#  We call some integer wonderful if it is a permutation of the digits in num 
# and is greater in value than num. There can be many wonderful integers. However, 
# we only care about the smallest-valued ones. 
# 
#  
#  For example, when num = "5489355142": 
#  
# 
#  
#  The 1ˢᵗ smallest wonderful integer is "5489355214". 
#  The 2ⁿᵈ smallest wonderful integer is "5489355241". 
#  The 3ʳᵈ smallest wonderful integer is "5489355412". 
#  The 4ᵗʰ smallest wonderful integer is "5489355421". 
#  
#  
# 
# 
#  Return the minimum number of adjacent digit swaps that needs to be applied 
# to num to reach the kᵗʰ smallest wonderful integer. 
# 
#  The tests are generated in such a way that kᵗʰ smallest wonderful integer 
# exists. 
# 
#  
#  Example 1: 
#
#  
# Input: num = "5489355142", k = 4
# Output: 2
# Explanation: The 4ᵗʰ smallest wonderful number is "5489355421". To get this 
# number:
# - Swap index 7 with index 8: "5489355142" -> "5489355412"
# - Swap index 8 with index 9: "5489355412" -> "5489355421"
#  
# 
#  Example 2: 
# 
#  
# Input: num = "11112", k = 4
# Output: 4
# Explanation: The 4ᵗʰ smallest wonderful number is "21111". To get this number:
# 
# - Swap index 3 with index 4: "11112" -> "11121"
# - Swap index 2 with index 3: "11121" -> "11211"
# - Swap index 1 with index 2: "11211" -> "12111"
# - Swap index 0 with index 1: "12111" -> "21111"
#  
# 
#  Example 3: 
# 
#  
# Input: num = "00123", k = 1
# Output: 1
# Explanation: The 1ˢᵗ smallest wonderful number is "00132". To get this number:
# 
# - Swap index 3 with index 4: "00123" -> "00132"
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= num.length <= 1000 
#  1 <= k <= 1000 
#  num only consists of digits. 
#  
# 
#  Related Topics Two Pointers String Greedy 👍 712 👎 88


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        target = num
        for _ in range(k):
            target = self.next_permutation(target)
        target = list(target)
        num = list(num)
        res = 0
        for i in range(len(num)):
            if num[i] == target[i]:
                continue
            j = i

            while num[j] != target[i]:
                j += 1

            while j != i:
                num[j], num[j - 1] = num[j - 1], num[j]
                j -= 1
                res += 1
        return res

    def next_permutation(self, num: str) -> str:
        num = list(num)
        i = len(num) - 1
        while i > 0:
            if num[i - 1] < num[i]:
                break
            i -= 1

        i -= 1
        j = len(num) - 1
        while j > i:
            if num[j] > num[i]:
                break
            j -= 1
        num[i], num[j] = num[j], num[i]
        num[i + 1:] = num[i + 1:][::-1]
        return ''.join(num)
# leetcode submit region end(Prohibit modification and deletion)
