'''
Longest Common Substring | DP-29
Given two strings ‘X’ and ‘Y’, find the length of the longest common substring.
Examples :

Input : X = “GeeksforGeeks”, y = “GeeksQuiz”
Output : 5
The longest common substring is “Geeks” and is of length 5.

Input : X = “abcdxyz”, y = “xyzabcd”
Output : 4
The longest common substring is “abcd” and is of length 4.

Input : X = “zxabcdezy”, y = “yzabcdezx”
Output : 6
The longest common substring is “abcdez” and is of length 6.
'''
def get_logest_substring(x,y):
    n=len(x)
    m=len(y)
    longest=0
    for i in range(n):
        count=0
        for j in range(m):
            while i+count<n and j+count<n and x[i+count]==y[j+count]:
                count++
            longest=max(count,longest)
    return longest