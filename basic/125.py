# 验证回文符

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ''.join(c.lower() for c in s if c.isalnum())
        return t == t[::-1]

for s in ["A man, a plan, a canal: Panama", "race a car"]:
    print(Solution().isPalindrome(s))
