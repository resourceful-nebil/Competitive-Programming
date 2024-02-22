class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono = []
        ans = [0] * len(temperatures)
        for i,n in enumerate(temperatures):
            
            while mono and mono[-1][1] < n:
                ind,val = mono.pop()
                ans[ind] = i - ind
            
            mono.append([i,n])

        return ans