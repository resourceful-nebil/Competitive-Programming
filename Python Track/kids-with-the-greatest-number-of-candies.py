class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx = max(candies)
        result = []
        for i,num in enumerate(candies):
            extra_plus = candies[i] + extraCandies
            if extra_plus < mx:
                result.append(False)
            else:
                result.append(True)
        return result 
