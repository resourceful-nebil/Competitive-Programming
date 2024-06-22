class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        di = defaultdict(int)
        count = 0
        prefix = 0
        di[prefix] = 1

        for i in range(len(nums)):
            prefix += nums[i] & 1
            diff = prefix - k

            if diff in di:
                count += di[diff]
            
            di[prefix] += 1
        
        return count 


        
