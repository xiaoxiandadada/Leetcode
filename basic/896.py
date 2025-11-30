# 单调数列
from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False
            if nums[i] < nums[i - 1]:
                increasing = False
        return increasing or decreasing

for i in [ [1,2,2,3], [6,5,4,4], [1,3,2], [1,2,4,5], [1,1,1] ]:
    print(Solution().isMonotonic(i))

