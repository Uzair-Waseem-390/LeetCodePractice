class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0] * n
        prev = float('-inf')
        
        # First pass: Left to Right
        for i in range(n):
            if s[i] == c:
                prev = i
            result[i] = i - prev if prev != float('-inf') else float('inf')
        
        # Second pass: Right to Left
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            result[i] = min(result[i], prev - i)
        
        return result
