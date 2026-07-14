from collections import defaultdict
from typing import List
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = defaultdict(list)
#         for s in strs:
#             groups[''.join(sorted(s))].append(s)
#         return list(groups.values())


class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26  # 26个字母的计数器
            for ch in s:
                index = ord(ch) - ord('a')
                count[index] += 1

            groups[tuple(count)].append(s)

        return list(groups.values())

res= Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)