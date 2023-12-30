class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # Finding the minimum and maximum cost of ice creams
        min_cost = min(costs)
        max_cost = max(costs)

        # Calculating the range of costs
        range_val = max_cost - min_cost + 1

        # Initializing a count array for counting occurrences of each cost
        count = [0] * range_val

        # Counting the occurrences of each cost using counting sort logic
        for num in costs:
            count[num - min_cost] += 1

        # Modifying the count array to represent the positions of sorted costs
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Creating an output array with sorted costs based on counting sort
        output = [0] * len(costs)
        for num in costs[::-1]:
            output[count[num - min_cost] - 1] = num
            count[num - min_cost] -= 1
        
        # Determining the maximum number of affordable ice creams within the budget
        total_cost = 0
        num_ice_creams = 0
        for cost in output:
            total_cost += cost
            if total_cost > coins:
                break
            num_ice_creams += 1

        return num_ice_creams
