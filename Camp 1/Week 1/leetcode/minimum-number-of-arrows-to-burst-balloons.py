class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        x = -inf
        no_of_arrows = 0
        points.sort(key = lambda x: (x[0],x[1]))
        print(points)            

        for i in range(n):
            if x < points[i][0]:
                no_of_arrows += 1
                x = points[i][1]
            else:
                x = min(x,points[i][1])

        return no_of_arrows
