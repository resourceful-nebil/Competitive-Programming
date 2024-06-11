class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        ind = 0  # Initialize the index pointer for swapping
        
        # Iterate over each element in arr2
        for num in arr2:
            # Iterate over each element in arr1
            for i in range(len(arr1)):
                if num == arr1[i]:  # If the element in arr1 matches the current element in arr2
                    # Swap the element at ind with the matching element
                    arr1[ind], arr1[i] = arr1[i], arr1[ind]
                    ind += 1  # Increment the index pointer
        
        # Sort the remaining elements in arr1
        arr1[ind:len(arr1)] = sorted(arr1[ind:len(arr1)])
     
        return arr1