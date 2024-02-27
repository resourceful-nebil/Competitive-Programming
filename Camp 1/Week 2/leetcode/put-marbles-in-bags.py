class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        pair_arr = sorted(a + b for a, b in itertools.pairwise(weights))

        sum_of_largest = sum(heapq.nlargest(k -1, pair_arr))

        sum_of_smallest = sum(heapq.nsmallest(k - 1, pair_arr))

        return sum_of_largest - sum_of_smallest

################Simpler way
# if k == 1:
#     return 0
# sums = sorted([weights[i] + weights[i + 1] for i in range(len(weights) - 1)])
# return sum(sums[-k + 1:]) - sum(sums[:k - 1])