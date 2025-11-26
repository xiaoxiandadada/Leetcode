# 移动零
from typing import List 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in  range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k+=1
        for i in range(k,len(nums)):
            nums[i]=0


Sol=Solution()
for nums in ([0,1,0,3,12],[0]):
    Sol.moveZeroes(nums)
    print(nums)