class Solution:
    def maxCoins(self, piles):
        # Sort the 'piles' list in ascending order
        piles.sort()

        # Get the total number of piles
        n = len(piles)

        # Initialize the variable to store the total number of coins obtained
        ans = 0

        # Start from the second largest pile (index n - 2)
        j = n - 2

        # Loop through a third of the total piles
        for i in range(n // 3):
            # Add the number of coins from every other pile (starting from the second largest)
            ans += piles[j]

            # Move two steps back to consider the next pile to be added
            j -= 2

        # Return the total number of coins obtained
        return ans
