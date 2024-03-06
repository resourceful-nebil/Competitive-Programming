# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # nums = [i for i in range(1,n + 1)]
        # if n == 1:
        #     return n
        l,r = 0 , n

        while l + 1 < r:
            mid = (l + r) //2

            if isBadVersion(mid):
                r = mid
            else:
                l = mid 
            
        return r
        
        # for i in range(1,n+1):
        #     if self.isBadVersion(i) and n != 0:
        #         while self.isBadVersion(i - 1):
