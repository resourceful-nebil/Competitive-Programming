class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Extract x-coordinates from points
        x_coordinates = [point[0] for point in points]

        # Sort the x-coordinates
        sorted_x_coordinates = sorted(x_coordinates)

        # Initialize a variable to store the maximum width
        max_width = 0

        # Iterate through the sorted x-coordinates to find the maximum width
        for i in range(1, len(sorted_x_coordinates)):
            # Calculate the width between consecutive x-coordinates
            width = sorted_x_coordinates[i] - sorted_x_coordinates[i - 1]

            # Update max_width if the calculated width is greater
            if width > max_width:
                max_width = width

        # Return the maximum width found
        return max_width
