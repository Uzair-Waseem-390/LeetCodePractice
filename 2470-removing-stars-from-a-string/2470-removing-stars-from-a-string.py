class Solution:
    def removeStars(self, s: str) -> str:
        c = []
        for i in s:
            if c and i == "*":
                c.pop()
            else:
                c.append(i)
        return ''.join(c)