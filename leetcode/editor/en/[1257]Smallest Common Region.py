# You are given some lists of regions where the first region of each list 
# directly contains all other regions in that list. 
# 
#  If a region x contains a region y directly, and region y contains region z 
# directly, then region x is said to contain region z indirectly. Note that region 
# x also indirectly contains all regions indirectly containd in y. 
# 
#  Naturally, if a region x contains (either directly or indirectly) another 
# region y, then x is bigger than or equal to y in size. Also, by definition, a 
# region x contains itself. 
# 
#  Given two regions: region1 and region2, return the smallest region that 
# contains both of them. 
# 
#  It is guaranteed the smallest region exists. 
# 
#  
#  Example 1: 
# 
#  
# Input:
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# Output: "North America"
#  
# 
#  Example 2: 
# 
#  
# Input: regions = [["Earth", "North America", "South America"],["North 
# America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", 
# "Ontario", "Quebec"],["South America", "Brazil"]], region1 = "Canada", region2 =
#  "South America"
# Output: "Earth"
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= regions.length <= 10⁴ 
#  2 <= regions[i].length <= 20 
#  1 <= regions[i][j].length, region1.length, region2.length <= 20 
#  region1 != region2 
#  regions[i][j], region1, and region2 consist of English letters. 
#  The input is generated such that there exists a region which contains all 
# the other regions, either directly or indirectly. 
#  A region cannot be directly contained in more than one region. 
#  
# 
#  Related Topics Array Hash Table String Tree Depth-First Search Breadth-First 
# Search 👍 487 👎 42


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        g = {}
        for region in regions:
            x = region[0]
            for y in region[1:]:
                g[y] = x

        s = set()
        x = region1
        while x in g:
            s.add(x)
            x = g[x]
        y = region2
        while y in g and y not in s:
            y = g[y]
        return y

# leetcode submit region end(Prohibit modification and deletion)
