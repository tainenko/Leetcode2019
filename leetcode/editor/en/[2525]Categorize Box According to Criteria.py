# Given four integers length, width, height, and mass, representing the 
# dimensions and mass of a box, respectively, return a string representing the category 
# of the box. 
# 
#  
#  The box is "Bulky" if: 
#  
# 
#  
#  Any of the dimensions of the box is greater or equal to 10⁴. 
#  Or, the volume of the box is greater or equal to 10⁹. 
#  
#  
#  If the mass of the box is greater or equal to 100, it is "Heavy". 
#  If the box is both "Bulky" and "Heavy", then its category is "Both". 
#  If the box is neither "Bulky" nor "Heavy", then its category is "Neither". 
#  If the box is "Bulky" but not "Heavy", then its category is "Bulky". 
#  If the box is "Heavy" but not "Bulky", then its category is "Heavy". 
# 
# 
#  Note that the volume of the box is the product of its length, width and 
# height. 
# 
#  
#  Example 1: 
# 
#  
# Input: length = 1000, width = 35, height = 700, mass = 300
# Output: "Heavy"
# Explanation: 
# None of the dimensions of the box is greater or equal to 10⁴. 
# Its volume = 24500000 <= 10⁹. So it cannot be categorized as "Bulky".
# However mass >= 100, so the box is "Heavy".
# Since the box is not "Bulky" but "Heavy", we return "Heavy". 
# 
#  Example 2: 
# 
#  
# Input: length = 200, width = 50, height = 800, mass = 50
# Output: "Neither"
# Explanation: 
# None of the dimensions of the box is greater or equal to 10⁴.
# Its volume = 8 * 10⁶ <= 10⁹. So it cannot be categorized as "Bulky".
# Its mass is also less than 100, so it cannot be categorized as "Heavy" either.
#  
# Since its neither of the two above categories, we return "Neither". 
# 
#  
#  Constraints: 
# 
#  
#  1 <= length, width, height <= 10⁵ 
#  1 <= mass <= 10³ 
#  
# 
#  Related Topics Math 👍 133 👎 35


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = length >= 10 ** 4 or width >= 10 ** 4 or height >= 10 ** 4 or length * width * height >= 10 ** 9
        is_heavy = mass >= 100
        if is_bulky and is_heavy:
            return "Both"
        elif not is_bulky and not is_heavy:
            return "Neither"
        elif is_bulky:
            return "Bulky"
        else:
            return "Heavy"
# leetcode submit region end(Prohibit modification and deletion)
