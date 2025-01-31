class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            n = sum(int(digit) ** 2 for digit in str(n))
            if n == 1: 
                return True
            elif n in seen: 
                return False
            seen.add(n)