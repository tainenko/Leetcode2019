#Given a list of non negative integers, arrange them such that they form the largest number. 
#
# Example 1: 
#
# 
#Input: [10,2]
#Output: "210" 
#
# Example 2: 
#
# 
#Input: [3,30,34,5,9]
#Output: "9534330"
# 
#
# Note: The result may be very large, so you need to return a string instead of an integer. 
#

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = sorted([str(x) for x in nums], key=self.cmp_to_key(self.cmp))
        res = ''
        for val in nums:
            res += val
        return res.lstrip('0')

    def cmp(self, x, y):
        xy = int(x + y)
        yx = int(y + x)
        return (yx > xy) - (yx < xy)

    def cmp_to_key(self, mycmp):
        'Convert a cmp= function into a key= function'

        class K:
            def __init__(self, obj, *args):
                self.obj = obj

            def __lt__(self, other):
                return mycmp(self.obj, other.obj) < 0

            def __gt__(self, other):
                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0

            def __eq__(self, other):
                return mycmp(self.obj, other.obj) == 0

            def __le__(self, other):
                return mycmp(self.obj, other.obj) <= 0

            def __ge__(self, other):
                return mycmp(self.obj, other.obj) >= 0

            def __ne__(self, other):
                return mycmp(self.obj, other.obj) != 0

        return K
