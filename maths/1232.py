# 缀点成线
from typing import List
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 取前两个点
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        # 基准向量
        dx = x1 - x0
        dy = y1 - y0

        # 检查每个点是否与前两个点共线
        for x, y in coordinates[2:]:
            # (x - x0, y - y0) 与 (dx, dy) 共线 ⇔ 叉积 = 0
            if dx * (y - y0) != dy * (x - x0):
                return False
        
        return True

Solution = Solution()
print(Solution.checkStraightLine([[1,2],[2,3],[3,4]]))