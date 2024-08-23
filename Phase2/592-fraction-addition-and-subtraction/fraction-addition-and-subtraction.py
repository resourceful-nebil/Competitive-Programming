class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator, common_denominator = 0, 1
        for d in range(2, 11):
            common_denominator *= d  
      
        if expression[0].isdigit():
            expression = '+' + expression
      
        i, expr_length = 0, len(expression)
        while i < expr_length:
            sign = -1 if expression[i] == '-' else 1
            i += 1  
          
           
            j = i
            while j < expr_length and expression[j] not in '+-':
                j += 1
          
            # Extract the current fraction
            fraction_str = expression[i:j]
            numerator_str, denominator_str = fraction_str.split('/')
          
            # Update the combined numerator
            numerator += sign * int(numerator_str) * common_denominator // int(denominator_str)
          
            # Move to the start of the next fraction
            i = j
      
        # Reduce the fraction by the greatest common divisor
        common_divisor = gcd(numerator, common_denominator)
        numerator //= common_divisor
        common_denominator //= common_divisor
      
        # Return the reduced fraction as a string
        return f'{numerator}/{common_denominator}'