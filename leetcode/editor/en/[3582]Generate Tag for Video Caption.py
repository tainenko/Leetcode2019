# You are given a string caption representing the caption for a video. 
# 
#  The following actions must be performed in order to generate a valid tag for 
# the video: 
# 
#  
#  Combine all words in the string into a single camelCase string prefixed with 
# '#'. A camelCase string is one where the first letter of all words except the 
# first one is capitalized. All characters after the first character in each word 
# must be lowercase. 
#  Remove all characters that are not an English letter, except the first '#'. 
#  Truncate the result to a maximum of 100 characters. 
#  
# 
#  Return the tag after performing the actions on caption. 
# 
#  
#  Example 1: 
# 
#  
#  Input: caption = "Leetcode daily streak achieved" 
#  
# 
#  Output: "#leetcodeDailyStreakAchieved" 
# 
#  Explanation: 
# 
#  The first letter for all words except "leetcode" should be capitalized. 
# 
#  Example 2: 
# 
#  
#  Input: caption = "can I Go There" 
#  
# 
#  Output: "#canIGoThere" 
# 
#  Explanation: 
# 
#  The first letter for all words except "can" should be capitalized. 
# 
#  Example 3: 
# 
#  
#  Input: caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" 
#  
# 
#  Output: "#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
# hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh" 
# 
#  Explanation: 
# 
#  Since the first word has length 101, we need to truncate the last two 
# letters from the word. 
# 
#  
#  Constraints: 
# 
#  
#  1 <= caption.length <= 150 
#  caption consists only of English letters and ' '. 
#  
# 
#  Related Topics String Simulation 👍 25 👎 15


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateTag(self, caption: str) -> str:
        ans = ["#"]
        to_upper = False
        for i, c in enumerate(caption):
            if len(ans) > 99:
                break
            if c == " ":
                to_upper = True
            if not c.isalpha():
                continue
            if to_upper:
                ans.append(c.upper())
                to_upper = False
            else:
                ans.append(c.lower())
            ans[1] = ans[1].lower()
        return "".join(ans)

# leetcode submit region end(Prohibit modification and deletion)
