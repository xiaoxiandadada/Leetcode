# 交替合并字符串
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # merge=[]
        # j=max(len(word2),len(word1))
        # i=min(len(word2),len(word1))
        
        # if len(word1) <= len(word2):
        #     for i in range(len(word1)):
        #         merge.append(word1[i])
        #         merge.append(word2[i])
        #     merge.append(word2[i+1:j])
        
        # if len(word1) > len(word2):
        #     for i in range(len(word2)):
        #         merge.append(word1[i])
        #         merge.append(word2[i])
        #     merge.append(word1[i+1:j])
        
        # return "".join(merge)


        # res=[]
        # i=j=0
        # while i < len(word1) or j < len(word2):
        #     if i < len(word1):
        #         res.append(word1[i])
        #         i += 1
        #     if j < len(word2):
        #         res.append(word2[j])
        #         j += 1
        # return "".join(res)

        res=[]
        for a,b in zip(word1,word2):
            res +=[a,b]
        return "".join(res)+word1[len(word2):]+word2[len(word1):]
        
        
        
sol=Solution()
for word1,word2 in [("abc","pqr"),("ab","pqrs"),("abcd","pq")]:
    print(sol.mergeAlternately(word1,word2))