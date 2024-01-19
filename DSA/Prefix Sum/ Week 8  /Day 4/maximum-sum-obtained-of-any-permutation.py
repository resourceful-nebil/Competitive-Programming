class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        d = [0] * len(nums)

        for l,r in requests:
            d[l] += 1

            if r + 1 < len(nums):
                d[r + 1] -= 1

        for i in range(1,len(d)):
            d[i] += d[i - 1]

        nums.sort()
        d.sort()

        modulus = 10**9 + 7

        total_sum = sum(a * b for a,b in zip(nums,d))

        return total_sum % modulus
