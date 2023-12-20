class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        v = []
        var = ''.join(map(str,digits))
        num = int(var)
        num += 1
        s = str(num)
        v=map(int,list(s))
        return v
       