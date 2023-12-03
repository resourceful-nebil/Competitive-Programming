class Solution:
    def romanToInt(self, s: str) -> int:
        di={"I": 1,"V":5, "X" : 10 , "L" : 50 , "C" : 100 , "D": 500 , "M": 1000}
        ans=0

        for i,j in zip(s,s[1:]):
            if di[i] < di[j]:
                ans-=di[i]
            else:
                ans+=di[i]
        return ans + di[s[-1]]
            
            
            

            
