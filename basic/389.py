## 找不同
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        for ch in s:
            x ^= ord(ch)
        for ch in t:
            x ^= ord(ch)
        return chr(x)
 
    # return chr(sum(map(ord, t)) - sum(map(ord, s)))

s = "abcd"
t = "abcde"
Sol=Solution()
print(Sol.findTheDifference(s,t))