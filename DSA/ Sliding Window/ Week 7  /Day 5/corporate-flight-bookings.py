class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0] * (n + 1)
        ans = []

        for f,l,s in bookings:
            prefix_sum[f-1] += s
            prefix_sum[l] -= s
        prefix = 0
        for i in range(len(prefix_sum)):
            prefix += prefix_sum[i]
            ans.append(prefix)
        
        return ans[:-1]


        