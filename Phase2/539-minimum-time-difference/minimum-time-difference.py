class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert(time):
            h,m = map(int,time.split(":"))
            time = (h*60) + m
            return time
        
        minu = [convert(time) for time in timePoints]

        minu.sort()
        # print(minu)

        minDifference = float('inf')
        for i in range(1, len(minu)):
            difference = minu[i] - minu[i - 1]
            minDifference = min(minDifference, difference)
        
        circular = minu[0] + (1440 - minu[-1])
        minDifference = min(minDifference, circular)



        return minDifference

        
        
