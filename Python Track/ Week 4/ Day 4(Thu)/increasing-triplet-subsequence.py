class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x = float('inf')
        y = float('inf')
      
        # makes x and y holds the min values and in the 3rd returns true 
        for i in range(len(nums)):
            if x >= nums[i]:
                x = nums[i]
            elif y >= nums[i]:
                y = nums[i]
            else:
                return True 
         
        return False 
        