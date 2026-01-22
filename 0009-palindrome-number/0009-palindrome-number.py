class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # return s == s[::-1]
        if x < 0:
            return False
        else:
            num = x
            ans = 0
            while num > 0:
                last_number = num % 10
                ans = ans * 10 + last_number
                num = num // 10
            return ans == x