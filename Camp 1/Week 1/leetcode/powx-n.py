class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x,-n)
        num = self.myPow(x, n//2) 
    
        if n % 2 == 0:
            return (num * num)
        else:
            return (num * num * x)
        
