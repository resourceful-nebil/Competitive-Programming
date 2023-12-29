class Solution:
    def sortSentence(self, s: str) -> str:
        
        # Split the input string into a list of words
        s = s.split()
        
        # Create a list to store words in their respective positions
        ans = [""] * len(s)
        
        # Iterate through each word in the input string
        for i in s:
            # Extract the last character of the word (which represents the position)
            position = int(i[-1]) - 1  # Convert position to 0-indexed
            
            # Store the word in its correct position in the 'ans' list
            # by using the position mentioned in the word itself
            ans[position] = i[:-1]  # Exclude the last character (which is the position)
        
        # Join the words in 'ans' list to form a sentence and return
        return ' '.join(ans)
