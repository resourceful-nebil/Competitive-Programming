class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xs = reduce(xor,nums)
        lb = xs & -xs # to get least significant beat

        a = 0
        for x in nums:
            if x & lb:
                a ^= x
        
        # xs = a ^ b
        b = a ^ xs
        return [a,b]