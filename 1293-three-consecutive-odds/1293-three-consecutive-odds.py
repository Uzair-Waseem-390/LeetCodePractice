class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        c = 0
        a = []
        for i in range(len(arr) -2):
            if arr[i] % 2 != 0 and arr[i+1] % 2 != 0 and arr[i+2] % 2 != 0:
                return True
        return False
            
                
                
                
