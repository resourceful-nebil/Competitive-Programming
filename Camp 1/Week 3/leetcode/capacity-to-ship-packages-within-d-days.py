class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def helper(capacity):
            days = 1
            ans = 0
            for w in weights:
                ans += w
                if ans > capacity:
                    days += 1
                    ans = w
      
            return days 



        l,r = max(weights),sum(weights)

        while l <= r:
            # print(l,r)
            mid = (l + r) //2

            if helper(mid) <= days:
                r = mid-1
            else:
                l = mid + 1
            
        return l