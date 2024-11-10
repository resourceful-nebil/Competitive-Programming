class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the list of people in ascending order
        people.sort()
        
        boats = 0  # Number of boats needed
        i = 0  # Pointer for the lightest person
        j = len(people) - 1  # Pointer for the heaviest person

        # Iterate until both pointers meet or cross each other
        while i <= j:
            # Calculate the weight difference between the limit and the heaviest person
            diff = limit - people[j]
            j -= 1  # Move the heaviest person pointer to the next person
            
            # Check if the weight of the lightest person is less than or equal to the difference
            if people[i] <= diff:
                i += 1  # Move the lightest person pointer to the next person
            
            boats += 1  # Increment the boat count
        
        return boats  # Return the number of boats used