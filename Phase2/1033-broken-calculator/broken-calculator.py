class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        op = 0
      
        while startValue < target:
            if target % 2:
                target += 1
            else:
                target >>= 1
            op += 1
      
        op += startValue - target
      
        return op
        