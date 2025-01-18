class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        s = list(num)
        for i in range(len(s)-1, -1, -1):
            if s[i] != "0":
                break
            else:
                s.pop(i)
        return ''.join(s)