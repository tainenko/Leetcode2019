# The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand. 
# 
#  
#  For example, "#15c" is shorthand for the color "#1155cc". 
#  
# 
#  The similarity between the two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)² 
# - (CD - WX)² - (EF - YZ)². 
# 
#  Given a string color that follows the format "#ABCDEF", return a string 
# represents the color that is most similar to the given color and has a shorthand (i.
# e., it can be represented as some "#XYZ"). 
# 
#  Any answer which has the same highest similarity as the best answer will be 
# accepted. 
# 
#  
#  Example 1: 
# 
#  
# Input: color = "#09f166"
# Output: "#11ee66"
# Explanation: 
# The similarity is -(0x09 - 0x11)² -(0xf1 - 0xee)² - (0x66 - 0x66)² = -64 -9 -0
#  = -73.
# This is the highest among any shorthand color.
#  
# 
#  Example 2: 
# 
#  
# Input: color = "#4e3fe1"
# Output: "#5544dd"
#  
# 
#  
#  Constraints: 
# 
#  
#  color.length == 7 
#  color[0] == '#' 
#  color[i] is either digit or character in the range ['a', 'f'] for i > 0. 
#  
#  Related Topics Math String Enumeration 👍 76 👎 469


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def similarRGB(self, color: str) -> str:
        
# leetcode submit region end(Prohibit modification and deletion)
