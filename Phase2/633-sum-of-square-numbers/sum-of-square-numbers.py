class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        while left <= right:
            _sum = left ** 2 + right ** 2

            if _sum == c:
                return True 
            elif _sum < c:
                left += 1
            else:
                right -= 1
        
        return False