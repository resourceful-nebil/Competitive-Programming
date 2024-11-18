class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        ans = []  # List to store the indices of pancake flips
        
        n = len(arr)  # Number of elements in the array
        k = 0  # Variable to store the index of the largest element in the current iteration

        while n > 1:  # Loop until there is only one element remaining
        
            k = arr.index(n)  # Find the index of the largest element in the current iteration
           
            # Flip the subarray from the beginning up to the largest element (inclusive)
            arr = arr[:k+1][::-1] + arr[k+1:]
            
            # Flip the entire array to move the largest element to the beginning
            arr = arr[:n][::-1] + arr[n:]
            
            ans.append(k+1)  # Append the index of the largest element to the answer list
            ans.append(n)  # Append the current value of n (number of elements) to the answer list
            n -= 1  # Decrement the number of elements by 1 in each iteration
        
        return ans  # Return the list of pancake flips