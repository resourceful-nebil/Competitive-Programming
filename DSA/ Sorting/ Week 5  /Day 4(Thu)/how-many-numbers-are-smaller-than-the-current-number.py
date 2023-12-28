class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mp = {}  # Create an empty dictionary to store the numbers and their counts
        n = len(nums)  # Get the length of the nums list
        snum = nums.copy()  # Create a copy of the nums list
        
        snum.sort()  # Sort the copied list in ascending order
        for i in range(n-1, -1, -1):  # Iterate over the sorted list in reverse order
            mp[snum[i]] = i  # Assign the index i to the number snum[i] in the dictionary
        
        for i in range(n):  # Iterate over the original nums list
            nums[i] = mp[nums[i]]  # Replace each element with its count from the dictionary
        
        return nums  # Return the modified nums list