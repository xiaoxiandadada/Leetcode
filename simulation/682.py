# 棒球比赛
from typing import List
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            match i:
                case '+':
                    stack.append(stack[-1]+stack[-2])
                case 'D':
                    stack.append(2*stack[-1])
                case 'C':
                    stack.pop()
                case _:
                    stack.append(int(i))
        return sum(stack)

for ops in [["5","2","C","D","+"],["5","-2","4","C","D","9","+","+"],["1"]]:
    print(Solution().calPoints(ops))