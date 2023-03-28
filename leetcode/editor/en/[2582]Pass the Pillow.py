# There are n people standing in a line labeled from 1 to n. The first person 
# in the line is holding a pillow initially. Every second, the person holding the 
# pillow passes it to the next person standing in the line. Once the pillow reaches 
# the end of the line, the direction changes, and people continue passing the 
# pillow in the opposite direction. 
# 
#  
#  For example, once the pillow reaches the nᵗʰ person they pass it to the n - 1
# ᵗʰ person, then to the n - 2ᵗʰ person and so on. 
#  
# 
#  Given the two positive integers n and time, return the index of the person 
# holding the pillow after time seconds. 
#  
#  Example 1: 
# 
#  
# Input: n = 4, time = 5
# Output: 2
# Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 
# 3 -> 2.
# Afer five seconds, the pillow is given to the 2ⁿᵈ person.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3, time = 2
# Output: 3
# Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
# Afer two seconds, the pillow is given to the 3ʳᵈ person.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= n <= 1000 
#  1 <= time <= 1000 
#  
# 
#  Related Topics Math Simulation 👍 248 👎 11


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)
