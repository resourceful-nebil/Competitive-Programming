class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window_size = n - k  # Determine the size of the sliding window from the opposite end
        min_sum = sum(cardPoints[:window_size])  # Initialize the minimum sum as the sum of the first window

        # Calculate the initial sum of the window
        window_sum = sum(cardPoints[:window_size])

        # Iterate through the remaining windows
        for i in range(window_size, n):
            window_sum += cardPoints[i] - cardPoints[i - window_size]  # Slide the window by adding the next card and removing the first card
            min_sum = min(min_sum, window_sum)  # Update the minimum sum if necessary

        total_sum = sum(cardPoints)  # Calculate the sum of all cards
        max_sum = total_sum - min_sum  # Calculate the maximum sum by subtracting the minimum sum

        return max_sum


        