class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l,r = 0, citations[-1]

        while l <= r:
            mid = (l + r)//2
            idx = bisect_left(citations,mid)

            if len(citations) - idx >= mid:
                l = mid + 1
            else:
                r = mid - 1
        
        return r 