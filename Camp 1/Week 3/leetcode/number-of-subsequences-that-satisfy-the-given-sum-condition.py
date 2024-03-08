class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        
        for i in range(len(nums)):
            r = len(nums)-1
            l = i
            while l <= r:
                mid = (l + r)//2

                if nums[i] + nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            if l - i:
                ans += 2**(l - i - 1)


        return ans % (10**9 + 7)