class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join(map(str, digits))
        s = str(int(s) + 1)
        ans = []
        for i in s:
            ans.append(int(i))
        return ans
