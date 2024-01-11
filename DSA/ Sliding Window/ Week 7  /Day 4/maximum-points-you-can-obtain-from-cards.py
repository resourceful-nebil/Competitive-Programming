class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Calculate the sum of all the cards
        total = sum(cardPoints)

        # Determine the size of the sliding window from the opposite end
        windowSize = len(cardPoints) - k

        # Calculate the sum of the first window
        windowSum = sum(cardPoints[:windowSize])
        minWindow = windowSum  # Initialize the minimum sum as the sum of the first window

        # Iterate through the remaining windows
        for i in range(windowSize, len(cardPoints)):
            # Slide the window by adding the next card and removing the first card
            windowSum += cardPoints[i] - cardPoints[i - windowSize]
            minWindow = min(minWindow, windowSum)  # Update the minimum sum if necessary

        # Calculate the maximum sum by subtracting the minimum sum from the total sum
        return total - minWindow