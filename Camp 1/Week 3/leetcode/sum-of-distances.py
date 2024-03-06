class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        di = {}

        for i in range(len(nums)):
            if nums[i] in di:
                idx,cnt = di[nums[i]]
                amount = (i - idx)*cnt + ans[idx]
                ans[i] += amount
                di[nums[i]] = (i,cnt+1)
            else:
                di[nums[i]] = (i,1)

        di = {}
        suffix = [0] * len(nums)      
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in di:
                idx,cnt = di[nums[i]]
                amount = (idx - i)*cnt + suffix[idx]
                suffix[i] += amount
                di[nums[i]] = (i,cnt+1)
            else:
                di[nums[i]] = (i,1)
        for i in range(len(nums)):
            ans[i] += suffix[i]
        
        # print(ans)
        # print(suffix)
        return ans

        
