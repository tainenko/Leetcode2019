'''
[859] Buddy Strings

https://leetcode.com/problems/buddy-strings/description/

* algorithms
* Easy (27.66%)
* Source Code:       859.buddy-strings.py
* Total Accepted:    27K
* Total Submissions: 97.3K
* Testcase Example:  '"ab"\n"ba"'

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:



Input: A = "ab", B = "ba"
Output: true



Example 2:


Input: A = "ab", B = "ab"
Output: false



Example 3:


Input: A = "aa", B = "aa"
Output: true



Example 4:


Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true



Example 5:


Input: A = "", B = "aa"
Output: false


 

Note:


        0 <= A.length <= 20000
        0 <= B.length <= 20000
        A and B consist only of lowercase letters.

'''


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # 解題思路
        # 如果 A和B的長度不相等，return False
        # 遍歷A B,統計有幾個不相等的字符，並記錄不相等的字符index
        # case1 diff=0，A B字串相同，需要檢查字串裡是否有重覆出現的字母
        # case2 diff==2，檢查兩個位置的字符是否交叉相等。
        # case3 其他情況，A B字串不可能為buddy String，return False
        if len(A) != len(B):
            return False
        diff = 0
        idx = []
        for i in range(len(A)):
            if B[i] != A[i]:
                diff += 1
                idx.append(i)
        flag = dict()
        if diff == 0:
            for letter in A:
                if flag.get(letter, None):
                    return True
                else:
                    flag[letter] = True
        elif diff == 2:
            return A[idx[0]] == B[idx[1]] and A[idx[1]] == B[idx[0]]
        else:
            return False
