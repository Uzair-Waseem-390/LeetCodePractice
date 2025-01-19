from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = Counter(stones)
        s = 0
        for key,value in c.items():
            if key in jewels:
                s = s + value
        return s