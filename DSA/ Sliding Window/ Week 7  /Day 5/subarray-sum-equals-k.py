class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        di = defaultdict(int)
        count = 0
        prefix = 0
        di[prefix] = 1

        for num in nums:
            prefix += num
            diff = prefix - k

            if diff in di:
                count += di[diff]
            di[prefix] += 1
        
        return count


       
                




            
