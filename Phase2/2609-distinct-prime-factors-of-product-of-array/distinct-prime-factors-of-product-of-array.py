class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        n = 1
        for num in nums:
            n *= num

        factorization: list[int] = []
        d = 2
        while d * d <= n:
            while n % d == 0:            
                factorization.append(d)
                n //= d
            d += 1
        if n > 1:
                factorization.append(n) 

        return len(set(factorization))