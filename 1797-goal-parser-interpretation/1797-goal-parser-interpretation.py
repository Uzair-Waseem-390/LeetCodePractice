class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                ans += "G"
                i += 1
            elif command[i] == "a":
                ans += "al"
                i += 3
            elif command[i] == "(" and command[i+1] == ")":
                ans += "o"
                i += 2
            else:
                i += 1
        return ans