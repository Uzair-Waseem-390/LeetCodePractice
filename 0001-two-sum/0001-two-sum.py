class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i,v in enumerate(nums):
            x = target - v
            if x in c:
                return (c[x], i)
            else:
                c[v] = i
        # for i,v1 in enumerate(nums):
        #     for j,v2 in enumerate(nums):
        #         if v1+v2==target and i != j:
        #             return i,j