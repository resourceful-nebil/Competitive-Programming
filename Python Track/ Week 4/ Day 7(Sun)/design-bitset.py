class Bitset:
    def __init__(self, size: int):
        # Initialize two lists: 'original' stores '0's, 'reversed' stores '1's
        self.original = ['0'] * size
        self.reversed = ['1'] * size  
        self.cot = 0  # 'cot' stores the count of '1's in 'original'

    def fix(self, idx: int) -> None:
        # If the bit at 'idx' in 'original' is '0', increment the count 'cot'
        if self.original[idx] == '0':
            self.cot += 1
        # Set the bit at 'idx' to '1' in 'original' and '0' in 'reversed'
        self.original[idx] = '1'
        self.reversed[idx] = '0'

    def unfix(self, idx: int) -> None:
        # If the bit at 'idx' in 'original' is '1', decrement the count 'cot'
        if self.original[idx] == '1':
            self.cot -= 1
        # Set the bit at 'idx' to '0' in 'original' and '1' in 'reversed'
        self.original[idx] = '0'
        self.reversed[idx] = '1'

    def flip(self) -> None:
        # Swap 'original' and 'reversed' lists and update 'cot' by subtracting current count from total size
        self.original, self.reversed = self.reversed, self.original
        self.cot = len(self.original) - self.cot

    def all(self) -> bool:
        # Check if the count 'cot' is equal to the length of 'original' (all bits are set to '1')
        return self.cot == len(self.original)

    def one(self) -> bool:
        # Return True if 'cot' is not zero (at least one bit is set to '1' in 'original')
        return self.cot

    def count(self) -> int:
        # Return the count of '1's in 'original'
        return self.cot

    def toString(self) -> str:
        # Convert 'original' list to a string and return it
        return ''.join(self.original)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
