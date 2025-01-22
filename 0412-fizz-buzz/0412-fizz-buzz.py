class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0 and i > 14:
                ans.append("FizzBuzz")
            elif i % 5 == 0 and i > 4:
                ans.append("Buzz")
            elif i % 3 == 0 and i > 2:
                ans.append("Fizz")
            else:
                ans.append(str(i))
        return ans