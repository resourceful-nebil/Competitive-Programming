class Solution:
    def smallestValue(self, n: int) -> int:
        if n <= 5:
            return n

        factorization: list[int] = []
        d = 2
        while d * d <= n:
            while n % d == 0:            
                factorization.append(d)
                n //= d
            d += 1
        if n > 1:
            factorization.append(n)
        if len(factorization) == 1:
            return factorization[0]
        else:
            # return 0
            return self.smallestValue(sum(factorization))
        



        

