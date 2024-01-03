class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the lists of children and available candies in ascending order
        g.sort()
        s.sort()
        
        # Get the lengths of the sorted lists
        n = len(g)  # number of children
        m = len(s)  # number of available candies
        
        # Initialize variables
        count = 0  # count of content children
        i = 0  # index for children list
        j = 0  # index for candies list

        # Iterate until all children are considered or all candies are exhausted
        while i < n:
            while j < m and i < n:
                if g[i] > s[j]:  # if the current child's greed is greater than the available candy
                    j += 1  # move to the next available candy
                else:
                    count += 1  # increment the count of content children
                    j += 1  # move to the next available candy
                    i += 1  # move to the next child
            break  # exit the loop

        return count