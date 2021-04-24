# Given a characters array tasks, representing the tasks a CPU needs to do, wher
# e each letter represents a different task. Tasks could be done in any order. Eac
# h task is done in one unit of time. For each unit of time, the CPU could complet
# e either one task or just be idle.
#
#  However, there is a non-negative integer n that represents the cooldown perio
# d between two same tasks (the same letter in the array), that is that there must
#  be at least n units of time between any two same tasks.
#
#  Return the least number of units of times that the CPU will take to finish al
# l the given tasks.
#
#
#  Example 1:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
#
#
#  Example 2:
#
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
#
#
#  Example 3:
#
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle ->
#  idle -> A
#
#
#
#  Constraints:
#
#
#  1 <= task.length <= 104
#  tasks[i] is upper-case English letter.
#  The integer n is in the range [0, 100].
#
#  Related Topics Array Greedy Queue
#  👍 4664 👎 884

from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = Counter(tasks)
        most_freq = counter.most_common()[0][1]
        common = sum(val == most_freq for val in counter.values())
        return max(len(tasks), (most_freq - 1) * (1 + n) + common)

# leetcode submit region end(Prohibit modification and deletion)
