class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        operation_count = 0


        for i in range(len(nums)-1):

            if nums[i] > nums[i+1]:
                operation_count += 1

                if i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
                
                if operation_count > 1:
                    return False
        return True

            
                