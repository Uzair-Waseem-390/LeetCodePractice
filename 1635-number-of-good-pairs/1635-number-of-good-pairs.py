class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i,v1 in enumerate(nums):
            for j,v2 in enumerate(nums):
                if i < j and v1 == v2:
                    ans += 1
        return ans