# 35. 搜索插入位置
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
            # if nums[i]==target:
            #     return i

            # if nums[i] > target:
            #    return i
        for i,num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)



nums = [1,3,5,6]
for target in [5,2,7]:
    sol = Solution()
    print(sol.searchInsert(nums, target))