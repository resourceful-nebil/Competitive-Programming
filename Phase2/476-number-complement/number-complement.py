class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)
        # print(b)
        pre = b[:2]
        b = b[2:]
        # print(b)
        # b ^ 
        # 
        b = list(map(int,b))
        for i in range(len(b)):
            b[i] = 1 - b[i]
            b[i] = str(b[i])
        


        # print(b)
        pre += ''.join(b)
        return int(pre,2)