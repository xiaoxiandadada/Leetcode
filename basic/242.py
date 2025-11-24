# 字母异位词
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"
Sol=Solution()
print(Sol.isAnagram(s,t))