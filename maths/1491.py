# 去掉最低工资和最高工资后的平均工资
from typing import List
class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        trimmed_salary = salary[1:-1]
        return sum(trimmed_salary) / len(trimmed_salary)

Sol= Solution()
print(Sol.average([4000,3000,1000,2000]))