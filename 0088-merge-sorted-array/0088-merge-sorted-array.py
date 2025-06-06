class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1





# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         s = 0
#         f = 0
#         for i in range(n+m+1):
#             if nums1[s] <= nums2[f]:
#                 if nums1[s] == 0:
#                     nums1.insert(s, nums2[f])
#                     f+=1
#                 s+=1
#             else:
#                 nums1.insert(s, nums2[f])
#                 s+=1
#                 f+=1
#             if f == n:
#                 break
#             for i in range(len(nums1)):
#                 if 0 in nums1:
#                     nums1.remove(0)
#                 else:
#                     break