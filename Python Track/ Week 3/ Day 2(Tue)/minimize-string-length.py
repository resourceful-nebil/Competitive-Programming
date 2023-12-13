class Solution:
    def minimizedStringLength(self, s: str) -> int:

        # Using set for reapeating chars
        s = set(s)
        return len(s)