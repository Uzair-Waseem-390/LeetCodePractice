class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[ :len(s) // 2]
        b = s[len(s) // 2: ]
        ans = 0
        ans2 = 0
        a = a.lower()
        b = b.lower()
        v = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(a)):
            if a[i] in v:
                ans += 1
            if b[i] in v:
                ans2 += 1
        return ans == ans2