class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if needle not in haystack:
            return -1
        n, m = len(haystack), len(needle)
        for j in range(n - m + 1):
            for i in range(m):
                if haystack[j + i] != needle[i]:
                    break
            else:
                return j

haystack = "hello"
needle = "ll"
# haystack = "leetcode"
# needle = "leeto"
Sol=Solution()
print(Sol.strStr(haystack,needle))