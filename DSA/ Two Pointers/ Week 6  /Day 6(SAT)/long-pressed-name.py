class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Initialize pointers for 'name' and 'typed' strings
        i = 0 
        j = 0

        # Check for matching characters in both strings
        while i < len(name) and j < len(typed):
            # If characters match, move both pointers
            if name[i] == typed[j]:
                i += 1
                j += 1
            # If characters don't match and a long key press is detected in 'typed', move 'typed' pointer
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            # If no match found and not a long key press, return False
            else:
                return False
        
        # Handle extra characters in 'typed' due to long key presses
        while j < len(typed) and typed[j] == typed[j - 1]:
            j += 1
        
        # Check if both strings are fully traversed and matched
        return i == len(name) and j == len(typed)
