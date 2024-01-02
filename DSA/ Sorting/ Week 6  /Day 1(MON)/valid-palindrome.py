class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0  # Left pointer
        r = len(s) - 1  # Right pointer
        
        while l < r:  # Continue until left pointer surpasses right pointer
            if not s[l].isalnum():  # If character at the left pointer is not alphanumeric
                l += 1  # Move the left pointer to the right
            elif not s[r].isalnum():  # If character at the right pointer is not alphanumeric
                r -= 1  # Move the right pointer to the left
            else:
                if s[l].lower() != s[r].lower():  # Compare characters at the left and right pointers (ignoring case)
                    return False  # If characters are not equal, the string is not a palindrome
                l += 1  # Move the left pointer to the right
                r -= 1  # Move the right pointer to the left
        
        return True  # If the loop completes without returning False, the string is a palindrome