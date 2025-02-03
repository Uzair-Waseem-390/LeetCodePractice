class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = []
        for i in range(len(s)):
            ans.append(abs(i - t.index(s[i])))
        return sum(ans)