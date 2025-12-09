# 最富有客户的资产总量
from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            max_wealth = max(max_wealth, sum(accounts[i]))
        return max_wealth

Sol=Solution()
print(Sol.maximumWealth([[1,2,3],[3,2,1]]))