class Solution:
    def timeRequiredToBuy(self, v: List[int], k: int) -> int:
        n = len(v)
        t = 0
        while True:
            for i in range(n):
                if v[i] > 0:
                    v[i] -= 1
                    t += 1
                if i == k and v[i] == 0:
                    return t
                    
        # ans = 0
        # while True:
        #     c = tickets.pop(0)
        #     ans += 1
        #     if c - 1 != 0:
        #         tickets.append(c - 1)
        #     if len(tickets) == 0:
        #         break