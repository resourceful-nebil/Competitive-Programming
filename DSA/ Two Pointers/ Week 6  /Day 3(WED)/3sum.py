class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list for easier traversal and to find triplets efficiently
        nums.sort()
        
        # Use a set to store unique triplets (avoiding duplicates)
        ans = set()
        
        # Loop through the sorted list for the first element of the triplet
        for i in range(len(nums)):
            # Initialize pointers for the other two elements of the triplet
            j = i + 1
            k = len(nums) - 1
            
            # While the two pointers don't cross each other
            while j < k:
                # If the sum of three elements equals 0 and the triplet is unique
                if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j != k:
                    # Store the unique triplet in the set
                    triplet = (nums[i], nums[j], nums[k])
                    ans.add(triplet)
                    
                    # Move the pointers to potentially find other triplets
                    j += 1
                    k -= 1
                # If the sum is greater than 0, decrement 'k' to reduce the sum
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                # If the sum is less than 0, increment 'j' to increase the sum
                else:
                    j += 1
                    
        # Return the unique triplets that sum up to zero
        return ans
