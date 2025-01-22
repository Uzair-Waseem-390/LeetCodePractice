class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = [0, gain[0]]
        for i in range(1, len(gain)):
            ans.append(gain[i] + ans[-1])
        return max(ans)