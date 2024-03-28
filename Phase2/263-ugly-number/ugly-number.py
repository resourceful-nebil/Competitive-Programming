class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factorization: list[int] = []
        d = 2
        while d * d <= n:
            while n % d == 0:            
                factorization.append(d)
                n //= d
            d += 1
        if n > 1:
            factorization.append(n) 
        
        print(factorization)
        fact = set(factorization)

        check = [2,3,5]
        for f in fact:
            if f not in check:
                return False
        
        return True 