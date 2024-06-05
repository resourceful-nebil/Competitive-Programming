from collections import Counter  # Importing Counter class from collections module

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize a Counter for the first word to keep track of letter frequencies
        char_count = Counter(words[0])
      
        # Iterate through all words in the input list
        for word in words:
            # Create a Counter for the current word
            current_count = Counter(word)
          
            # Check all the characters in the initial word's counter
            for char in list(char_count):
                # Update the character's count to be the minimum of the current and the first word's count
                # This ensures we only keep as many of a character as is common to all words so far
                char_count[char] = min(char_count[char], current_count[char])
      
        # Initialize an empty list to hold the common characters
        common_characters = []
      
        # Iterate through the items in the final char_count
        for char, count in char_count.items():
            # For each character, add it to the list as many times as its count
            common_characters.extend([char] * count)
      
        # Return the list of common characters
        return common_characters