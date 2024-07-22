class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)

        memo = [float('inf')] * (1 << n)

        memo[0] = 0

        for bit in range(1,1 << n):
            k = bin(bit).count('1') - 1

            for j in range(n):
                if bit & (1 << j):
                    pre = bit ^ (1 << j)

                    memo[bit] = min(memo[bit],
                                    memo[pre] + (nums1[k] ^ nums2[j]) )

        return memo[-1]