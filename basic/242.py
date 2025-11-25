# 字母异位词
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return len(s) == len(t) and Counter(s) == Counter(t)

        c1 = {}
        c2 = {}
        
        for c in s:
            # if c in c1:
            #     c1[c] += 1
            # else:
            #     c1[c] = 1
            c1[c] = c1.setdefault(c,0) + 1
        for c in t:
            c2[c] = c2.setdefault(c,0) + 1
        
        return c1==c2
        



s = "anagram"
t = "nagaram"
Sol=Solution()
print(Sol.isAnagram(s,t))