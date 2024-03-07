class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        i, j = 0, 0
        max_d = 0

        while i < len(houses):
            while j < len(heaters) and houses[i] >= heaters[j]:
                j += 1

            if j == 0:
                max_d = max(max_d, heaters[j] - houses[i])
            elif j == len(heaters):
                max_d = max(max_d, houses[i] - heaters[j-1])
            else:
                max_d = max(max_d, min(heaters[j] - houses[i], houses[i] - heaters[j-1]))

            i += 1

        return max_d