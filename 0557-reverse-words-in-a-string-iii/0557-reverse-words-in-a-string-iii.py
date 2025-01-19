class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        ans = []
        for i in words:
            i = "".join(reversed(i))
            ans.append(i)
        return ' '.join(ans)
