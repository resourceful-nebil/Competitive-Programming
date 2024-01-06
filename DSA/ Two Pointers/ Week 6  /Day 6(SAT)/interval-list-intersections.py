class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []  # List to store the intersection intervals
        i = 0  # Pointer for firstList
        j = 0  # Pointer for secondList

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]  # Extract start and end points of the current interval in firstList
            start2, end2 = secondList[j]  # Extract start and end points of the current interval in secondList

            if end1 >= start2 and end2 >= start1:  # Check if there is an intersection
                intersection_start = max(start1, start2)  # Calculate the start point of the intersection interval
                intersection_end = min(end1, end2)  # Calculate the end point of the intersection interval

                intersection.append([intersection_start, intersection_end])  # Add the intersection interval to the result

            if end1 < end2:
                i += 1  # Move to the next interval in firstList
            else:
                j += 1  # Move to the next interval in secondList

        return intersection  # Return the list of intersection intervals

# two pointers on intersection
# knowing when to move the pointers based on ending 
# start 1, start 2, end1 and end2
# this is oreder of the lists if there is intersection