class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        # Combine the names and heights into pairs
        combined_pairs = list(zip(names, heights))
        n = len(names)

        # Perform bubble sort in descending order based on heights
        for i in range(n):
            for j in range(n - i - 1):
                # Compare the heights of two adjacent pairs
                if combined_pairs[j][1] < combined_pairs[j + 1][1]:
                    # Swap the pairs if the height is in descending order
                    combined_pairs[j], combined_pairs[j + 1] = combined_pairs[j + 1], combined_pairs[j]

        sorted_heights = []
        # Extract the sorted names from the combined pairs
        for pair in combined_pairs:
            sorted_heights.append(pair[0])

        return sorted_heights