# 转换成小写字母
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

for i in ["Hello", "here", "LOVELY"]:
    print(Solution().toLowerCase(i))