class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        * Total Submissions: 417.2K
        * Testcase Example:  '"A"'

        Given a column title as appear in an Excel sheet, return its corresponding column number.

        For example:


            A -> 1
            B -> 2
            C -> 3
            ...
            Z -> 26
            AA -> 27
            AB -> 28
            ...


        Example 1:


        Input: "A"
        Output: 1


        Example 2:


        Input: "AB"
        Output: 28


        Example 3:


        Input: "ZY"
        Output: 701

        """
        res=0
        for letter in s:
            res=26*(res+1)+ord(letter)-90
        return res
        
