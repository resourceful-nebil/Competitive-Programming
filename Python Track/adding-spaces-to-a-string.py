class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new_sttr = ""
        count = 0
        for i,ch in enumerate(s):
            if count<len(spaces) and spaces[count] == i:
                new_sttr += ' '
                count += 1
            new_sttr += ch
        
        return new_sttr