# You are given a 2D string array responses where each responses[i] is an array 
# of strings representing survey responses from the iᵗʰ day. 
# 
#  Return the most common response across all days after removing duplicate 
# responses within each responses[i]. If there is a tie, return the lexicographically 
# smallest response. 
# 
#  
#  Example 1: 
# 
#  
#  Input: responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],[
# "good"],["bad"]] 
#  
# 
#  Output: "good" 
# 
#  Explanation: 
# 
#  
#  After removing duplicates within each list, responses = [["good", "ok"], [
# "ok", "bad", "good"], ["good"], ["bad"]]. 
#  "good" appears 3 times, "ok" appears 2 times, and "bad" appears 2 times. 
#  Return "good" because it has the highest frequency. 
#  
# 
#  Example 2: 
# 
#  
#  Input: responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],[
# "great","good"]] 
#  
# 
#  Output: "bad" 
# 
#  Explanation: 
# 
#  
#  After removing duplicates within each list we have responses = [["good", 
# "ok"], ["ok", "bad"], ["bad", "notsure"], ["great", "good"]]. 
#  "bad", "good", and "ok" each occur 2 times. 
#  The output is "bad" because it is the lexicographically smallest amongst the 
# words with the highest frequency. 
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= responses.length <= 1000 
#  1 <= responses[i].length <= 1000 
#  1 <= responses[i][j].length <= 10 
#  responses[i][j] consists of only lowercase English letters 
#  
# 
#  Related Topics Array Hash Table String Counting 👍 28 👎 4


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnt = collections.Counter()
        for response in responses:
            for res in set(response):
                cnt[res] += 1
        ans = responses[0][0]
        for word, time in cnt.items():
            if cnt[ans] < time or cnt[ans] == time and word < ans:
                ans = word
        return ans
# leetcode submit region end(Prohibit modification and deletion)
