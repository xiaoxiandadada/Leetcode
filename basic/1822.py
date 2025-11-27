# 数组元素积的符号
from typing import List 
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                count +=1
        # if count % 2 ==1:
        #     return -1
        # if count % 2 ==0:
        #     return 1
        return 1-2*(count %2)


Sol=Solution()
for nums in ([-1,-2,-3,-4,3,2,1],[1,5,0,2,-3], [-1,1,-1,1,-1]):
    print(Sol.arraySign(nums))
        