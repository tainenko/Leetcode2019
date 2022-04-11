# You are given an array of strings strs. You could concatenate these strings 
# together into a loop, where for each string, you could choose to reverse it or 
# not. Among all the possible loops 
# 
#  Return the lexicographically largest string after cutting the loop, which 
# will make the looped string into a regular one. 
# 
#  Specifically, to find the lexicographically largest string, you need to 
# experience two phases: 
# 
#  
#  Concatenate all the strings into a loop, where you can reverse some strings 
# or not and connect them in the same order as given. 
#  Cut and make one breakpoint in any place of the loop, which will make the 
# looped string into a regular one starting from the character at the cutpoint. 
#  
# 
#  And your job is to find the lexicographically largest one among all the 
# possible regular strings. 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["abc","xyz"]
# Output: "zyxcba"
# Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-",
#  "-cbazyx-", where '-' represents the looped status. 
# The answer string came from the fourth looped one, where you could cut from 
# the middle character 'a' and get "zyxcba".
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["abc"]
# Output: "cba"
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 1000 
#  1 <= strs[i].length <= 1000 
#  1 <= sum(strs[i].length) <= 1000 
#  strs[i] consists of lowercase English letters. 
#  
#  Related Topics Array String Greedy 👍 62 👎 236


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def splitLoopedString(self, strs: List[str]) -> str:
        strs = [s if s > s[::-1] else s[::-1] for s in strs]
        res = ""
        for i, s in enumerate(strs):
            left = "".join(strs[:i])
            right = "".join(strs[i + 1:])
            for target in [s, s[::-1]]:
                for j in range(len(target)):
                    res = max(res, target[j:] + right + left + target[:j])
        return res

# leetcode submit region end(Prohibit modification and deletion)
