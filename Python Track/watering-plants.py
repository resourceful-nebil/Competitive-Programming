class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        remaining_water = capacity

        for i in range(len(plants)):
            
            if remaining_water >= plants[i]:
                remaining_water -= plants[i]
            else:
                remaining_water = capacity - plants[i]
                steps += i*2

        steps += len(plants)
        return steps
            

           

            