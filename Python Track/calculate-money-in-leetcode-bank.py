class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        count = 0

        for weeks in range(1,n):
            for days in range(1,8):
                total += weeks
                weeks += 1
                count += 1
                if count == n:
                    return total
        
    
        return 1
                     
