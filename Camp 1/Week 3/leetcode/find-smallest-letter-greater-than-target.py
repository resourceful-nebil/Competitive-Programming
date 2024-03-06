class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        l = 0
        r = len(letters) - 1

        while l <= r:
            mid = (r + l)//2

            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return letters[l%len(letters)]