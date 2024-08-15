class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        n = len(bills)
        five = 0
        ten = 0
        twenty = 0
        i = 0
        while i < n:
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10:
                if five == 0:
                    return False
                ten += 1
                five -= 1
            elif bills[i] == 20:
                if five == 0:
                    return False
                elif ten == 0:
                    if five > 2:
                        twenty += 1
                        five -= 3
                    else:
                        return False
                else:
                    ten -= 1
                    five -= 1
                    twenty += 1
            else:
                return False
 
                    
            i += 1
        return True 

            
