class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = [0] * 24  
        pairs = 0
        
        for hour in hours:
            remainder = hour % 24
            complement = (24 - remainder) % 24
            pairs += count[complement]
            count[remainder] += 1
        
        return pairs


        
        
        
        # c = Counter(hours)
        # for key,value in c.items():
