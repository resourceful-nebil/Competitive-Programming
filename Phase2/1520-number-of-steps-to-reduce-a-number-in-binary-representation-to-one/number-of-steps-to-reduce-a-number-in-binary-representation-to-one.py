class Solution:
    def numSteps(self, s: str) -> int:
        i = int(s,2)
        cnt = 0

        def reduce(n):
            nonlocal cnt
            if n == 1:
                return 
            if n % 2 == 0:
                cnt += 1
                n = reduce(n // 2)
            else:
                cnt += 1
                n = reduce(n + 1)
            

        # print(int(s,2))
        reduce(i)
        return cnt