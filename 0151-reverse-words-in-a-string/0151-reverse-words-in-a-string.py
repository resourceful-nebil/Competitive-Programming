class Solution:
    def reverseWords(self, s: str) -> str:

        # store elements based on space 
        reverse_string = s.split()
       
        # reverse the string
        reverse_string = reverse_string[::-1]

        # return the reversed string with space between words
        return " ".join(reverse_string)