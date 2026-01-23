class Solution:
    def convertToBase7(self, num: int) -> str:
        re = ""
        if num == 0:
            return "0"
        if num < 0:
            num = abs(num)
            while num > 0:
                re =  str(num % 7)+ re
                num = num // 7
            
            return "-" + re

        while num > 0:
            re =  str(num % 7)+ re
            num = num // 7
        return re