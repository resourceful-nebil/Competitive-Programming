class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x,y):
            if y == 1:
                return x
            if y == 0:
                return 1
            
            num = power(x,y//2) 
            if y % 2 == 0:
                return (num * num) % (10**9 + 7)
            else:
                return (num * num * x) % (10**9 + 7)
            
        
        even  = n // 2
        odd = (n // 2) + (n % 2)
        return (power(5,odd) * power(4,even)) % (10**9 + 7)


       
       
        # if n == 1:
        #     return 5
        # c =
        # def check(x):
        #     if (x % 2 == 0):
        #         c *= 5
        #         return c
        #     else:
        #         c *= 4
        #         return c
            
        
        