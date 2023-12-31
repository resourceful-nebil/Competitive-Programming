class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort the points based on their Euclidean distance from the origin (0, 0)
        points.sort(key=lambda p: sqrt(p[0] ** 2 + p[1] ** 2))
        
        # Initialize an empty list to store the k closest points
        near = []
        
        # Iterate k times to append the k closest points to the 'near' list
        for i in range(k):
            near.append(points[i])
        
        # Return the list of k closest points
        return near