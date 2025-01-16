class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = 0
        ans = []
        for i in nums:
            for j in nums:
                if i != j and j < i:
                    n = n + 1
            ans.append(n)
            n = 0
        return ans