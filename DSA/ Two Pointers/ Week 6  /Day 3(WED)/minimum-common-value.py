class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize variables
        mini = 0  # Placeholder value for the common element
        
        i = 0  # Index for nums1
        j = 0  # Index for nums2

        # Iterate until the end of either nums1 or nums2 is reached
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:  # If the elements at the current indices are equal
                return nums1[i]  # Return the common element
            else:
                if nums1[i] > nums2[j]:  # If the element in nums1 is greater than the element in nums2
                    j += 1  # Move to the next element in nums2
                else:  # If the element in nums1 is smaller than the element in nums2
                    i += 1  # Move to the next element in nums1

        return -1  # Return -1 if no common element is found