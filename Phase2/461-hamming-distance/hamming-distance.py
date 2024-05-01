class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        b = z.bit_count()
        return b