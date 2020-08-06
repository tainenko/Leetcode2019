#
# @lc app=leetcode id=535 lang=python
#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (79.12%)
# Likes:    661
# Dislikes: 1456
# Total Accepted:    108.6K
# Total Submissions: 136.1K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
# 
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk.
# 
# Design the encode and decode methods for the TinyURL service. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that a URL can be encoded to a tiny URL and the tiny URL can be
# decoded to the original URL.
# 
#

# @lc code=start
class Codec:
    count = 0

    def __init__(self):
        self.long_urls = {}
        self.short_urls = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.long_urls:
            return "http://http://tinyurl.com/" + self.long_urls[longUrl]
        self.count += 1
        count_no = str(self.count)
        self.long_urls[longUrl] = count_no
        self.short_urls[count_no] = longUrl
        return "http://http://tinyurl.com/" + count_no

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.short_urls[shortUrl.split("/")[-1]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
