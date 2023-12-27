class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []  # Initialize an empty list to store the common elements
        dict = Counter(nums1)  # Create a dictionary to count the occurrences of each element in nums1

        for i, nums in enumerate(nums2):  # Iterate over each element in nums2
            if dict[nums] > 0:  # If the current element is present in the dictionary (occurred in nums1)
                intersection.append(nums)  # Add the element to the intersection list
                dict[nums] -= 1  # Decrease the count of the element in the dictionary

        return intersection  # Return the list of common elements