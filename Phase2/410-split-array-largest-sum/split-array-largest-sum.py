class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def condition(capacity):
            split = 1
            total = 0

            for n in nums:
                total += n
                if total > capacity:
                    total = n
                    split += 1
                    if split > k:
                        return False

            return True
        
        l,r = max(nums),sum(nums)
        while l < r:
            mid = l + (r - l)//2
            
            if condition(mid):
                r = mid
            
            else:
                l = mid + 1
        
        return l
        