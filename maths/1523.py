# 在区间范围内统计奇数数目
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # res = []
        # for i in range(low, high+1):
        #     if i % 2 ==1:
        #         res.append(i)
        # return len(res)
        # memory limit exceeded

        # 计算从1到high的奇数个数
        def count_up_to(x: int) -> int:
            return (x+1) // 2

        return count_up_to(high) - count_up_to(low-1)

Sol= Solution()
print(Sol.countOdds(8,10))