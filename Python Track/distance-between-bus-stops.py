class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        mx = max(start,destination)
        mn = min(start,destination)
        subtotal= sum(distance[mn:mx])
        return min(subtotal,total - subtotal)
        
        