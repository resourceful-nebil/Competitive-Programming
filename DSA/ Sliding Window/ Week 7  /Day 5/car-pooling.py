class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix_sum = [0] * 1001
        ans = []

        for n,f,t in trips:
            prefix_sum[f] += n
            prefix_sum[t] -= n
        
        prefix = 0
        for i in range(len(prefix_sum)):
            prefix += prefix_sum[i]
            ans.append(prefix)
            if ans[i] > capacity:
                return False
        
        return True 

        

        