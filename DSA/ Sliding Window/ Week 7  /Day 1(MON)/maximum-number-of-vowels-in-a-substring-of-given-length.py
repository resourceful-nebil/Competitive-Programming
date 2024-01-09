class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        start = 0 
        end = k

        max_vowels = 0
        current_vowels = 0 

        # Count the number of vowels in the initial substring
        for i in range(start, end):
            if s[i] in vowels:
                current_vowels += 1

        # Set the initial max_vowels value
        max_vowels = current_vowels

        # Slide the window and update the counts
        while end < len(s):
            # Decrement current_vowels if the character at start is a vowel
            if s[start] in vowels:
                current_vowels -= 1
            # Increment current_vowels if the character at end is a vowel
            if s[end] in vowels:
                current_vowels += 1
            
            # Update max_vowels if necessary
            max_vowels = max(max_vowels, current_vowels)
            # Move the window
            start += 1
            end += 1
        
        return max_vowels