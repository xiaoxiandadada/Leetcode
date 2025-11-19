# 移除元素
from typing import List
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         if not nums:
#             return 0
#         new_nums = []
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 new_nums.append(nums[i])
#         return len(new_nums)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j+=1
        return j


nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
print(sol.removeElement(nums,val))