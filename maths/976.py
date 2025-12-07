# 三角形的最大周长
# 复杂度 O(N \log N), greedy algorithm
from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

Sol=Solution()
print(Sol.largestPerimeter([1,2,1,10]))
