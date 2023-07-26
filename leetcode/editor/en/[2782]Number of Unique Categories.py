# You are given an integer n and an object categoryHandler of class 
# CategoryHandler. 
# 
#  There are nelements, numbered from 0 to n - 1. Each element has a category, 
# and your task is to find the number of unique categories. 
# 
#  The class CategoryHandler contains the following function, which may help 
# you: 
# 
#  
#  boolean haveSameCategory(integer a, integer b): Returns true if a and b are 
# in the same category and false otherwise. Also, if either a or b is not a valid 
# number (i.e. it's greater than or equal to nor less than 0), it returns false. 
#  
# 
#  Return the number of unique categories. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 6, catagoryHandler = [1,1,2,2,3,3]
# Output: 3
# Explanation: There are 6 elements in this example. The first two elements 
# belong to category 1, the second two belong to category 2, and the last two 
# elements belong to category 3. So there are 3 unique categories.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 5, catagoryHandler = [1,2,3,4,5]
# Output: 5
# Explanation: There are 5 elements in this example. Each element belongs to a 
# unique category. So there are 5 unique categories.
#  
# 
#  Example 3: 
# 
#  
# Input: n = 3, catagoryHandler = [1,1,1]
# Output: 1
# Explanation: There are 3 elements in this example. All of them belong to one 
# category. So there is only 1 unique category.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 100 
#  
# 
#  Related Topics Union Find Counting 👍 13 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]
        p = list(range(n))
        for i in range(n):
            for j in range(i+1,n):
                if categoryHandler.haveSameCategory(i, j):
                    p[find(i)]=find(j)
        return sum([1 for i,v in enumerate(p) if i==v])
# leetcode submit region end(Prohibit modification and deletion)
