# 最小整数可被K整除
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        length = 1
        num = 1
        while num % k != 0:
            num = (num % k) * 10 + 1
            length += 1
        return length

k = 3
Sol = Solution()
print(Sol.smallestRepunitDivByK(k))