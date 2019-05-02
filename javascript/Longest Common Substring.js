/**

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
*/
var longest_common_substring= function(x,y)=>{
    let n=x.length;
    let m=y.length;
    let longest=0;
    for(let i=0; i<n;i++){
        let count=0;
        for(let j=0; j<m;j++){
            while(i+count<n && j+count<m && x[i+count]==y[j+count]){
                count++;
            }
            longest=longest<count?count:longest;
        }
    }
    return longest;
}