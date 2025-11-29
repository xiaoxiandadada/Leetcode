# 判断能否形成等差数列
from typing import List 
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] != arr[1]-arr[0]:
                return False
        return True

Sol = Solution()
for arr in ([3,5,1],[1,2,4]):
    print(Sol.canMakeArithmeticProgression(arr))

