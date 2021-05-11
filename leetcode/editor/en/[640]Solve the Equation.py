# Solve a given equation and return the value of 'x' in the form of a string "x=
# #value". The equation contains only '+', '-' operation, the variable 'x' and its
#  coefficient. You should return "No solution" if there is no solution for the eq
# uation, or "Infinite solutions" if there are infinite solutions for the equation
# .
#
#  If there is exactly one solution for the equation, we ensure that the value o
# f 'x' is an integer.
#
#
#  Example 1:
#  Input: equation = "x+5-3+x=6+x-2"
# Output: "x=2"
#  Example 2:
#  Input: equation = "x=x"
# Output: "Infinite solutions"
#  Example 3:
#  Input: equation = "2x=x"
# Output: "x=0"
#  Example 4:
#  Input: equation = "2x+3x-6x=x+2"
# Output: "x=-1"
#  Example 5:
#  Input: equation = "x=x+2"
# Output: "No solution"
#
#
#  Constraints:
#
#
#  3 <= equation.length <= 1000
#  equation has exactly one '='.
#  equation consists of integers with an absolute value in the range [0, 100] wi
# thout any leading zeros, and the variable 'x'.
#
#  Related Topics Math
#  👍 294 👎 595


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        num1, x1 = self.calculate(left)

        num2, x2 = self.calculate(right)
        num = num2 - num1
        x = x1 - x2
        if x == 0 and num == 0:
            return "Infinite solutions"
        elif x == 0 and num:
            return "No solution"
        else:
            return "x={}".format(num / x)

    def calculate(self, expression):
        nums = []
        x = []
        tmp = ""
        for char in expression:
            if char == 'x':
                if tmp == '+' or tmp == '-' or not tmp:
                    tmp += '1'
                x.append(int(tmp))
                tmp = ""
                continue
            if (char == '+' or char == '-') and tmp:
                nums.append(int(tmp))
                tmp = char
                continue
            tmp += char
        if tmp:
            nums.append(int(tmp))
        return sum(nums), sum(x)

# leetcode submit region end(Prohibit modification and deletion)
