# 矩阵对角线元素的和
from typing import List
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total= 0
        for i in range(n):
            total +=mat[i][i]
            if i != n - i - 1:
                total += mat[i][n - i - 1]
        return total

mats=[[[1,2,3],
            [4,5,6],
            [7,8,9]],
            [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]],
            [[5]]]
Sol=Solution()
for mat in mats:
    print(Sol.diagonalSum(mat))