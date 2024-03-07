class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = 0

        def helper(divisor):
            total = 0
            for num in nums:
                total += (ceil(num/divisor))
            return total
        

        l, r = 1, max(nums)

        while l <= r:
            mid = (l + r)//2

            if helper(mid) <= threshold:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans