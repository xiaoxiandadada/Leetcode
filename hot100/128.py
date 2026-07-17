# 最长连续序列
from typing import List 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num = set(nums)

        ans = 0

        for x in num:

            if x-1 not in num:

                length = 1

                while x+length in num:
                    length += 1

                ans = max(ans,length)

        return ans

nums = [100, 4, 200, 1, 3, 2]
res = Solution().longestConsecutive(nums)
print(res)
