class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = []
        for i in range(1, len(nums)):
            ans.append(abs(nums[i-1] - nums[i]))
        ans.append(abs(nums[-1] - nums[0]))
        return max(ans)