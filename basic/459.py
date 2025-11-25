# 重复的字符串
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # n = len(s)
        # if n <= 1:
        #     return False
        # str = ""

        # for i in range(1,len(s)//2 +1):
        #     str=s[:i]
        #     if (len(s)//i) * str == s and len(s)%i == 0:
        #         return True
        # return False
        return True if s in (s + s)[1:-1] else False


Sol=Solution()
for s in ("abcabcabcabc","abab", "aba","aaaa","a","abaababaab"):
    print(Sol.repeatedSubstringPattern(s))

