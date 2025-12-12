# 单词规律
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern)!=len(words):
            return False
        pdc,sdc ={},{}
        for p,w in zip(pattern,words):
            if p not in pdc:
                pdc[p] = w
            if w not in sdc:
                sdc[w] = p
            if pdc[p]!=w or sdc[w]!=p:
                return False
        return True