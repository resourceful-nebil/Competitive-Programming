class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)  # Get the length of the flips list
        binary_string = [0] * n  # Initialize a binary string list with all zeros
        count = 0  # Initialize a count variable to keep track of the number of times all bulbs are blue
        min_ = 0  # Initialize a variable to keep track of the minimum index of the next blue bulb

        for i in range(n):  # Iterate over each flip in the flips list
            binary_string[flips[i] - 1] = 1  # Set the corresponding index in the binary string to 1 (representing a flipped bulb)

            if min_ == flips[i] - 1:  # Check if the minimum index of the next blue bulb is the same as the current flip

                j = min_  # Initialize a pointer j to the minimum index
                while j < n and binary_string[j] != 0:  # Move the pointer j until we find a bulb that is not flipped
                    min_ += 1  # Update the minimum index of the next blue bulb
                    j += 1

                if min_ - 1 == i:  # Check if the minimum index of the next blue bulb is equal to the current index
                    count += 1  # Increment the count as all bulbs up to the current index are blue

        return count  # Return the count of times all bulbs are blue