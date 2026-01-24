class Solution:
    def maximum69Number (self, num: int) -> int:
        x = []
        n = num
        while n > 0:
            ln = n %  10
            x.insert(0, ln)
            n//=10
        ans = 0
        if 6 not in x:
            for i in x:
                ans = ans * 10 + i
            return ans
        else:
            for i in range(0, len(x)):
                if x[i] == 6:
                    x[i] = 9
                    break
            for i in x:
                ans = ans * 10 + i
            return ans