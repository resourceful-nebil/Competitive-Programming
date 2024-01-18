class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        di = defaultdict(int)
        count = 0
        prefix = 0
        di[prefix] = 1

        for num in nums:
            prefix += num
            diff = prefix - goal

            if diff in di:
                count += di[diff]
            di[prefix] += 1
        
        return count