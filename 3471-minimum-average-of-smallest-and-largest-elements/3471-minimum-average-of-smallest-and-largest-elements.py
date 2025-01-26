class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ans = []
        while len(nums) != 0:
            s = min(nums)
            l = max(nums)
            nums.remove(s)
            nums.remove(l)
            ans.append((s+l)/2)
        return min(ans)