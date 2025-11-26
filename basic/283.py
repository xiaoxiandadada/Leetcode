# 移动零
from typing import List 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k=0
        # for i in  range(len(nums)):
        #     if nums[i] != 0:
        #         nums[k] = nums[i]
        #         k+=1
        # for i in range(k,len(nums)):
        #     nums[i]=0
        n =len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] == 0 and nums[j+1] !=0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]


Sol=Solution()
for nums in ([0,1,0,3,12],[0]):
    Sol.moveZeroes(nums)
    print(nums)