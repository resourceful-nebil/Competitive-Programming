class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        #edge Caases
        #1. Considering the circular behavoir of the function
        # by itering over the array twice with modulo


        
        #Intialize Length of the array, number of ones, left pointer
        #current window size with ones and maximum window size 
        N = len(nums)
        count_ones = nums.count(1)
        l = 0
        current_window_ones, max_window_ones = 0, 0

        #Iterating over the list twice
        for r in range(2 * N):
        #Checking if the element is one
            if nums[r % N]:
                current_window_ones += 1
        #Move left pointer if the window size is > than number of ones
            if r - l + 1 > count_ones:
                current_window_ones -= nums[l % N]
                l += 1
        #Update the maximum window size 
            max_window_ones = max(max_window_ones,current_window_ones)
        #Return the difference between the maximum window size of one and number of ones
        return  count_ones - max_window_ones 
