class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        cl = []
        for i in nums:
            if i not in cl:
                cl.append(i)
            else:
                ans.append(i)
        return ans