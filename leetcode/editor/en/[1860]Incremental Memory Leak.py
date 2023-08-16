# You are given two integers memory1 and memory2 representing the available 
# memory in bits on two memory sticks. There is currently a faulty program running 
# that consumes an increasing amount of memory every second. 
# 
#  At the iᵗʰ second (starting from 1), i bits of memory are allocated to the 
# stick with more available memory (or from the first memory stick if both have the 
# same available memory). If neither stick has at least i bits of available 
# memory, the program crashes. 
# 
#  Return an array containing [crashTime, memory1crash, memory2crash], where 
# crashTime is the time (in seconds) when the program crashed and memory1crash and 
# memory2crash are the available bits of memory in the first and second sticks 
# respectively. 
# 
#  
#  Example 1: 
# 
#  
# Input: memory1 = 2, memory2 = 2
# Output: [3,1,0]
# Explanation: The memory is allocated as follows:
# - At the 1ˢᵗ second, 1 bit of memory is allocated to stick 1. The first stick 
# now has 1 bit of available memory.
# - At the 2ⁿᵈ second, 2 bits of memory are allocated to stick 2. The second 
# stick now has 0 bits of available memory.
# - At the 3ʳᵈ second, the program crashes. The sticks have 1 and 0 bits 
# available respectively.
#  
# 
#  Example 2: 
# 
#  
# Input: memory1 = 8, memory2 = 11
# Output: [6,0,4]
# Explanation: The memory is allocated as follows:
# - At the 1ˢᵗ second, 1 bit of memory is allocated to stick 2. The second 
# stick now has 10 bit of available memory.
# - At the 2ⁿᵈ second, 2 bits of memory are allocated to stick 2. The second 
# stick now has 8 bits of available memory.
# - At the 3ʳᵈ second, 3 bits of memory are allocated to stick 1. The first 
# stick now has 5 bits of available memory.
# - At the 4ᵗʰ second, 4 bits of memory are allocated to stick 2. The second 
# stick now has 4 bits of available memory.
# - At the 5ᵗʰ second, 5 bits of memory are allocated to stick 1. The first 
# stick now has 0 bits of available memory.
# - At the 6ᵗʰ second, the program crashes. The sticks have 0 and 4 bits 
# available respectively.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= memory1, memory2 <= 2³¹ - 1 
#  
# 
#  Related Topics Simulation 👍 195 👎 80


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 1
        while i <= max(memory1, memory2):
            if memory1 >= memory2:
                memory1 -= i
            else:
                memory2 -= i
            i += 1
        return [i, memory1, memory2]

    # leetcode submit region end(Prohibit modification and deletion)
