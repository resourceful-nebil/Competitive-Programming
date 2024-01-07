class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Length of the input string
        n = len(s)

        # Initialize the maximum length of the substring
        maxLength = 0

        # Pointers for the sliding window technique
        i, j = 0, 0

        # Set to store unique characters in the substring
        charSet = set()

        # Loop through the string with two pointers, i and j
        while i < n and j < n:
            # If the character at index j is not in the set
            if s[j] not in charSet:
                # Add the character at index j to the set
                charSet.add(s[j])

                # Move j to expand the window
                j += 1

                # Update the maximum length of substring
                maxLength = max(maxLength, j - i)

            else:
                # If character at index j already exists in set, remove character at index i
                charSet.remove(s[i])

                # Slide the window forward
                i += 1

        # Return the maximum length of substring without repeating characters
        return maxLength

# using set with sliding windows