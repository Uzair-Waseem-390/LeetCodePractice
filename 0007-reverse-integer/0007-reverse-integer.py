class Solution:
    def reverse(self, x: int) -> int:
        if len(str(x)) == 1:
            return x
        x = list(str(x))
        x.reverse()
        if x[0] == "0":
            x.pop(0)
        if x[len(x)-1] == "-":
            x.pop()
            x.insert(0,"-")
        if int(''.join(x)) <= 2147483647 and int(''.join(x)) >= -2147483648:
            return int(''.join(x))
        else:
            return 0