class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:

        my_distance = abs(target[0]) + abs(target[1])

        for i in range(len(ghosts)):
            distance_of_ghost = abs(target[0] - ghosts[i][0]) + abs(target[1] - ghosts[i][1])
            
            if distance_of_ghost <= my_distance:
                return False
        
        return True

        