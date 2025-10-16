class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) > 1:
            ans = 0
            for i in num:
                ans += int(i)
            num = str(ans)
        return int(num)