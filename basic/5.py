# 最长回文字串
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 0
        current_str = ''
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                # print(i,j,s[i:j])
                if self.isPalindrome(s[i:j]) and j - i > max_len:
                    max_len = j - i
                    current_str = s[i:j]
        return current_str

    def isPalindrome(self, s: str):
        return s == s[::-1]


