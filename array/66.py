# 加一
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str=''.join(map(str,digits))
        nums=int(digits_str)+1
        return [int(num) for num in str(nums)]

sol=Solution()
for digits in ([1,2,3],[4,3,2,1],[9]):
    print(sol.plusOne(digits))
