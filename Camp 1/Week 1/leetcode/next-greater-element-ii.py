class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        stack = []
        nums.extend(nums)

        for i in range(len(nums)):
            i = i % (len(nums) // 2)
            while stack and nums[i] > stack[-1][1]:
                idx,n = stack.pop()
                ans[idx] = nums[i]
            
            stack.append((i,nums[i]))
        
        return ans
            