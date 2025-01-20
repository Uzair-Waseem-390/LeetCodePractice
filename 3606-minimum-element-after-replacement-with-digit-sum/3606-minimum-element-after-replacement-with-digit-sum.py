class Solution:
    def minElement(self, nums: List[int]) -> int:
        a = []
        c = []
        l = []
        for i in nums:
            a.append(str(i))
        for i in a:
            for j in i:
                c.append(int(j))
            l.append(sum(c))
            c = []
        return min(l)