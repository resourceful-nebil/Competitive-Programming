class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        prof_cap = []
        heap = []
        for i in range(len(profits)):
            prof_cap.append([capital[i],profits[i]])
        
        prof_cap.sort(key = lambda x : -x[0])
        for i in range(k):
            
            while prof_cap and prof_cap[-1][0] <= w:
                heappush(heap,-prof_cap.pop()[1])
            if heap:
                x = heappop(heap)
                w += -(x)

        return w
        # print(prof_cap)
