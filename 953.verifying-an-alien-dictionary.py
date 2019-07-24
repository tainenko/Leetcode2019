'''
[953] Verifying an Alien Dictionary

https://leetcode.com/problems/verifying-an-alien-dictionary/description/

* algorithms
* Easy (55.61%)
* Source Code:       953.verifying-an-alien-dictionary.py
* Total Accepted:    24.6K
* Total Submissions: 44K
* Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 


Example 1:


Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.



Example 2:


Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.



Example 3:


Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


 

Note:


        1 <= words.length <= 100
        1 <= words[i].length <= 20
        order.length == 26
        All characters in words[i] and order are english lowercase letters.
'''


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j > len(words[i + 1]) - 1:
                    return False
                elif words[i][j]==words[i+1][j]:
                    continue
                elif self.compare(words[i][j],words[i+1][j],order):
                    break
                else:
                    return False
        return True

    def compare(self, char1, char2, order):
            return order.index(char1)<=order.index(char2)

