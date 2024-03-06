class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 1 , len(nums)-1
        if len(nums) <= 2:
            return min(nums)

        ans = nums[0]
        while l <= r:
            mid = (l + r) //2

            if nums[mid] <= ans:
                ans = min(nums[mid],ans)
                r = mid-1
            else:
                l = mid + 1
            
        return ans