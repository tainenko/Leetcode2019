# Given an integer n, return all the strobogrammatic numbers that are of length 
# n. You may return the answer in any order. 
# 
#  A strobogrammatic number is a number that looks the same when rotated 180 
# degrees (looked at upside down). 
# 
#  
#  Example 1: 
#  Input: n = 2
# Output: ["11","69","88","96"]
#  
#  Example 2: 
#  Input: n = 1
# Output: ["0","1","8"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 14 
#  
# 
#  Related Topics Array String Recursion 👍 826 👎 211


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        records = dict()
        records[1] = ["0", "1", "8"]
        records[2] = ["11", "69", "88", "96"]
        pair = ["00", "11", "69", "88", "96"]
        if n <= 2:
            return records[n]
        count = 3
        while count <= n:
            record = []
            if (count - 1) % 2 == 0:
                for num in records[count - 1]:
                    for item in records[1]:
                        record.append(num[:len(num) // 2] + item + num[len(num) // 2:])
            else:
                for num in records[count - 2]:
                    for item in pair:
                        record.append(num[:len(num) // 2] + item + num[len(num) // 2:])
            records[count] = record
            count += 1
        return records[n]
# leetcode submit region end(Prohibit modification and deletion)
