from collections import Counter
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # a = Counter(nums1)
        # b = Counter(nums2)
        # print(a,b)
        
        
        
        
        
        
        ans = [0,0]
        ans1 = []
        ans2 = []
        for i in range(len(nums1)):
            if not nums1[i] in nums2 and not nums1[i] in ans1:
                ans1.append(nums1[i])
        for i in range(len(nums2)):
            if not nums2[i] in nums1 and not nums2[i] in ans2:
                ans2.append(nums2[i])
        ans[0] = ans1
        ans[1] = ans2
        return ans