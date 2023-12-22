class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        ones = len(nums) - zeros
        ans = [0]
        leftZeros = 0
        leftOnes = 0 
        highestScore = ones

        for i,num in enumerate(nums):
            if num == 0:
                leftZeros += 1
            elif num == 1:
                leftOnes += 1
            
            rightOnes = ones - leftOnes
            score = leftZeros + rightOnes 

            if highestScore == score:
                ans.append(i + 1)
            elif highestScore < score:
                highestScore = score 
                ans = [i + 1]

        return ans 


         
    
      




