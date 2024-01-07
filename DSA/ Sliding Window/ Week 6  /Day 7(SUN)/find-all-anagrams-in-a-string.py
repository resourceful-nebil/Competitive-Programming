class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        count = [0] * 26  # Create a list to count characters in the English alphabet (a-z)

        if len(s) < len(p):  # If length of s is less than length of p, no anagrams possible
            return ans

        for c in p:  # Count characters in string p
            count[ord(c) - ord('a')] += 1
        
        l, r = 0, 0  # Initialize left and right pointers for the sliding window

        while r < len(s):  # Loop through the string s
            count[ord(s[r]) - ord('a')] -= 1  # Decrement count for the character at s[r]

            if count[ord(s[r]) - ord('a')] < 0:  # Check if excess character in window
                while count[ord(s[r]) - ord('a')] < 0:  # Adjust the window to remove excess character
                    count[ord(s[l]) - ord('a')] += 1  # Increment count for character at s[l]
                    l += 1  # Move left pointer to shrink the window
                r += 1  # Move right pointer

            elif r - l + 1 == len(p):  # If window size equals length of p
                ans.append(l)  # Append the starting index of an anagram
                count[ord(s[l]) - ord('a')] += 1  # Increment count for character at s[l]
                l += 1  # Move left pointer to slide the window
                r += 1  # Move right pointer

            else:  # If window size is less than length of p, expand the window
                r += 1  # Move right pointer

        return ans  # Return the list of starting indices of anagrams of p in s

# learned ord('a') is 97
# inner iteration to skip unwanted characters