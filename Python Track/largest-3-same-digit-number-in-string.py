class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(2,len(num)):
            if num[i-1] == num[i-2] and num[i-1] == num[i]:
                
                ans = max((ans),num[i-2:i+1])

        return ans