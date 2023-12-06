class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        min_value = float('inf')
       

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if i+j < min_value:
                        min_value = i+j
                        ans = [list1[i]]
                    elif i+j == min_value:
                        ans.append(list1[i])
                
        return ans