class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []
        for i in operations:
            if s and i == "C":
                s.pop()
            elif s and i =="D":
                s.append(s[-1] * 2)
            elif s and i == "+":
                 s.append(s[-1] + s[-2])
            else:
                s.append(int(i))
        return sum(s)