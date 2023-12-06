class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(len(nums)):
            apperance = nums.count(nums[i])

            if nums[i] in ans:
                continue
           
            if apperance > n // 3:
                ans.append(nums[i])
        
        return ans
        