class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        ans =  0
        for i,num in enumerate(nums) :
            if num == 1:
                count += 1
            else: 
                ans = max(count,ans)
                count = 0
        ans = max(count,ans)
        return ans
        