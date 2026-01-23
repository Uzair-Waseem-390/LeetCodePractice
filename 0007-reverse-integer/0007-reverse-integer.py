class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = abs(x)
            ans = 0
            while num > 0:
                ln = num % 10
                ans = ans * 10 + ln
                num //=10
            if ans < -2**31 or ans > 2**31 - 1:
                return 0
            return -ans
        else:
            num = x
            ans = 0
            while num > 0:
                ln = num % 10
                ans = ans * 10 + ln
                num //= 10
            if ans < -2**31 or ans > 2**31 - 1:
                return 0
            return ans
                