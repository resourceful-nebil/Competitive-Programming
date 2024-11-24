class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = [0]
        total = 0
        for n in gain:
            total += n
            prefix.append(total)
        
        return max(prefix)