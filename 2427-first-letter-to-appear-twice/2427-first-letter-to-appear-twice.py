from collections import Counter
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        u = set()
        for i in s:
            if i in u:
                return i
            u.add(i)