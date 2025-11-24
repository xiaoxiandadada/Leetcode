# 找出字符串中第一个匹配项的下标
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if len(needle) == 0:
        #     return 0
        # if needle not in haystack:
        #     return -1
        # n, m = len(haystack), len(needle)
        # for j in range(n - m + 1):
        #     for i in range(m):
        #         if haystack[j + i] != needle[i]:
        #             break
        #     else:
        #         return j

        # if needle == "":
        #     return 0
        
        # n, m = len(haystack), len(needle)
        # if m > n:
        #     return -1
        
        # for i in range(n - m + 1):
        #     # 切片 [i, i+m)
        #     if haystack[i:i + m] == needle:
        #         return i
        
        # return -1

## KMP 匹配
        if needle == "":
            return 0
        
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        
        # 1. 先构造 lps 数组
        lps = self.build_lps(needle)
        
        # 2. 开始匹配
        i = 0  # 指向 haystack
        j = 0  # 指向 needle
        
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                # needle 全部匹配完了
                if j == m:
                    return i - j   # 起始下标
            else:
                if j != 0:
                    # 利用 lps 跳转，而不是把 j 归零
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1
    
    def build_lps(self, pattern: str):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps


haystack = "hello"
needle = "ll"
# haystack = "leetcode"
# needle = "leeto"
Sol=Solution()
print(Sol.strStr(haystack,needle))