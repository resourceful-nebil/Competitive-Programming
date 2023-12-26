class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        combined_pairs = list(zip(names,heights))
        n = len(names)

        

        for i in range(n):
            for j in range(n-i-1):
                if combined_pairs[j][1] < combined_pairs[j+1][1]:
                    combined_pairs[j] , combined_pairs[j+1] = combined_pairs[j+1] , combined_pairs[j]

        sorted_heights = []
        for pair in combined_pairs:
            sorted_heights.append(pair[0])

        return sorted_heights



        # for i in range(len(names)):
        #     for j in rnage
