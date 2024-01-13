class Solution:
    def balancedString(self, s: str) -> int:
        # Initialize ans with the length of the string
        ans = len(s)  
        # Count the occurrences of each character
        count = collections.Counter(s) 
        # Start of the sliding window 
        l = 0  

        # Iterate through each character in the string
        for r, c in enumerate(s):
            # Decrease the count of the current character
            count[c] -= 1  

            # Shrink the window while it contains an excess of characters 'Q', 'W', 'E', 'R'
            while l < len(s) and all(count[c] <= len(s) // 4 for c in 'QWER'):
                # Update ans with the minimum length of the substring
                ans = min(ans, r - l + 1)  
                # Increase the count of the character at the start of the window
                count[s[l]] += 1 
                # Move the start of the window to the right 
                l += 1  
        # Return the minimum length of the substring to be replaced
        return ans  