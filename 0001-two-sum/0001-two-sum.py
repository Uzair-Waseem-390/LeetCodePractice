class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for key1, i in enumerate(nums):
            for key2, j in enumerate(nums):
                if i + j == target and key1 != key2:
                    ans.append(key2)
                    ans.append(key1)
                    return ans