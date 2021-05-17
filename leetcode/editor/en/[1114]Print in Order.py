# Suppose we have a class: 
# 
#  
# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
#  
# 
#  The same instance of Foo will be passed to three different threads. Thread A 
# will call first(), thread B will call second(), and thread C will call third(). 
# Design a mechanism and modify the program to ensure that second() is executed af
# ter first(), and third() is executed after second(). 
# 
#  Note: 
# 
#  We do not know how the threads will be scheduled in the operating system, eve
# n though the numbers in the input seem to imply the ordering. The input format y
# ou see is mainly to ensure our tests' comprehensiveness. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,2,3]
# Output: "firstsecondthird"
# Explanation: There are three threads being fired asynchronously. The input [1,
# 2,3] means thread A calls first(), thread B calls second(), and thread C calls t
# hird(). "firstsecondthird" is the correct output.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,3,2]
# Output: "firstsecondthird"
# Explanation: The input [1,3,2] means thread A calls first(), thread B calls th
# ird(), and thread C calls second(). "firstsecondthird" is the correct output.
#  
#  👍 740 👎 133


# leetcode submit region begin(Prohibit modification and deletion)
from time import sleep


class Foo(object):
    index = 0

    def __init__(self):
        pass

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        while True:
            if self.index == 0:
                # printFirst() outputs "first". Do not change or remove this line.
                printFirst()
                self.index += 1
                break
            sleep(0.01)

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        while True:
            if self.index == 1:
                # printSecond() outputs "second". Do not change or remove this line.
                printSecond()
                self.index += 1
                break
            sleep(0.01)

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        while True:
            if self.index == 2:
                # printThird() outputs "third". Do not change or remove this line.
                printThird()
                break
            sleep(0.01)
# leetcode submit region end(Prohibit modification and deletion)
