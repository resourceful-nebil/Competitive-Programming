class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        t = 0
        for i in range(len(points)-1):
            d1 = abs(points[i][0] - points[i+1][0]) 
            d2 = abs(points[i][1] - points[i+1][1])
            d = max(d1,d2)
            print(d)
            t += d
        return t
         

            
