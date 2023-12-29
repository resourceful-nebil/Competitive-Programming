from collections import Counter

class Solution:
    def smallestNumber(self, num: int) -> int:
        
        ans = []
        if num >= 0:  # If the number is non-negative
            # Convert the number to a list of its digits
            num = list(map(int, str(num)))
            
            # Count the occurrence of each digit using Counter
            dicti = Counter(num)
            
            # Arrange digits in ascending order
            for i in range(10):
                if i in dicti:
                    # Append the digit to the 'ans' list based on its count in the number
                    while dicti[i] != 0:
                        ans.append(i)
                        dicti[i] -= 1
            
            # Move the first non-zero digit to the beginning to create the smallest number
            for i in range(len(ans)):
                if ans[i] != 0:
                    ans[0], ans[i] = ans[i], ans[0]
                    break

            # Convert the list of digits back to an integer and return
            return int(''.join(map(str, ans)))

        else:  # If the number is negative
            # Make the number positive
            num = -1 * num
            
            # Convert the number to a list of its digits and sort in descending order
            num = list(map(int, str(num)))
            num.sort(reverse=True)

            # Convert the sorted digits back to an integer and make it negative
            return int(''.join(map(str, num))) * -1
