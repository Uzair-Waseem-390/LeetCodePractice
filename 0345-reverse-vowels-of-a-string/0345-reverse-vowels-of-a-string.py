class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s)-1
        a = "AEIOUaeiou"
        u = list(s)
        while left < right:
            if s[left] in a and s[right] in a:
                u[left], u[right] = u[right], u[left]
                left += 1
                right -=1
                continue
            if not s[left] in a:
                left += 1
            if not s[right] in a:
                right -=1
        return ''.join(u)