class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        if len(word1) < len(word2):
            l = len(word2)
            c = word2
            s = len(word1)
        else:
            l = len(word1)
            c = word1
            s = len(word2)
        ans = []
        for i in range(l):
            if i < s:
                ans.append(word1[i])
                ans.append(word2[i])
            else:
                ans.append(c[i])
        return ''.join(ans)