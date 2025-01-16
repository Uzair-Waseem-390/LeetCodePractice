class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0
        for i in range(len(endTime)):
            if endTime[i] >= queryTime and startTime[i] <= queryTime:
                ans += 1
        return ans