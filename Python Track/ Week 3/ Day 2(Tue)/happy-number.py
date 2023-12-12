class Solution:
    def isHappy(self, n: int) -> bool:
        repeated = {}

        while n > 0:
            temp = 0
            """
            used to split the number by iterating based on the number of digits of the number until it's zero
            for example: 
            n = 19
            n % 10 = 9 -> to get the 1st number 
            and then square it 
            n // 10 = 1.9 == 1 -> by floor division to get the left digit 


            """
            while n != 0:
                left_digit = n % 10
                left_digit **= 2
                temp += left_digit
                n //= 10

            # checks if temp is already found because it creates an infinite loop
            if temp in repeated:
                return False

            # stores it in the hashmap 
            else:
                repeated[temp] = temp
            
            # checks the wanted result
            if temp == 1:
                return True 
            
            # resets n for another iteration
            n = temp 
        
        return False 