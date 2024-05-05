class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # Mask to limit values to 32 bits (to handle negative numbers)
        MAX_INT = 0x7FFFFFFF  # Maximum positive integer value
        
        while b != 0:
            # Perform bitwise XOR operation to get the sum without carry
            sum_without_carry = (a ^ b) & MASK
            
            # Perform bitwise AND operation and left shift by 1 to get the carry
            carry = ((a & b) << 1) & MASK
            
            # Update a and b for the next iteration
            a = sum_without_carry
            b = carry
        
        # If the result is a negative number, convert it to the correct negative representation
        if a > MAX_INT:
            a = ~(a ^ MASK)
        
        return a