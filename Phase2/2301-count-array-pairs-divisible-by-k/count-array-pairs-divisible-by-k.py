class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
        di = defaultdict(int)
        ans = 0

        for i in range(len(nums)):
            
            for key,items in di.items():
                if (nums[i] * key) % k == 0:
                    ans += items


            di[gcd(k,nums[i])] += 1 


        return ans 