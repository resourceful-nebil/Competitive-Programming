class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            ans = 0
            for p in piles:
                ans += (ceil(p/k))
            return ans

        l,r = 1,max(piles)
        ans = 0
        while l <= r:
            # print(l,r)
            mid = (l + r) //2

            if helper(mid) <= h:
                ans = mid
                r = mid-1
            else:
                l = mid + 1
            
        return ans