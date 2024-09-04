class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def condition(capacity):
            day = 1
            total = 0

            for w in weights:
                total += w
                if total > capacity:
                    total = w
                    day += 1
                    if day > days:
                        return False

            return True
        
        l,r = max(weights),sum(weights)
        while l < r:
            mid = l + (r - l)//2
            
            if condition(mid):
                r = mid
            
            else:
                l = mid + 1
        
        return l
