# 最后一个单词的长度
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        if not words:
            return 0
        return len(words[-1])

for i in ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy", ""]:
    print(Solution().lengthOfLastWord(i))