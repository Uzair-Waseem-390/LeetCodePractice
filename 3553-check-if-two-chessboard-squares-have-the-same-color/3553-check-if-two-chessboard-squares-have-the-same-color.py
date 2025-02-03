class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1,r1 = coordinate1[0],int(coordinate1[1])
        c2,r2 = coordinate2[0],int(coordinate2[1])
        c1 = ord(c1) - ord("a") + 1
        c2 = ord(c2) - ord("a") + 1
        if (c1 + r1) % 2 == 0:
            color1 = "Black"
        else:
            color1 = "White" 
        if (c2 + r2) % 2 == 0:
            color2 = "Black"
        else:
            color2 = "White" 
        return color1 == color2