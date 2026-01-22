class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans =[]
        ans2 = []
        final = set()
        c = 0
        for i in range(1, a//2):
            if a % i == 0:
                j = a/i
                if i != j:
                    ans.append(i)
                    ans.append(j)
                else:
                    ans.append(i)
                    break
        
        for i in range(1, b//2):
            if b % i == 0:
                j = b/i
                if i != j:
                    ans2.append(i)
                    ans2.append(j)
                else:
                    ans2.append(i)
                    break
        for i in ans:
            if i in ans2:
                final.add(i)
        if len(final) == 0:
            return len(final) + 1

        return len(final)
        