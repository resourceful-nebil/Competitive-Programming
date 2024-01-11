class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern = Counter(s1)
        l,r = 0,0

        count = 0

        while r < len(s2):
            if s2[r] in pattern:
                pattern[s2[r]] -= 1
                if pattern[s2[r]] == 0:
                    count += 1
            
            r += 1

            if r - l == len(s1):
                if count == len(pattern):
                    return True
                if s2[l] in pattern:
                    if pattern[s2[l]] == 0:
                        count -= 1
                    pattern[s2[l]] += 1
          
                l += 1
        
        return False 