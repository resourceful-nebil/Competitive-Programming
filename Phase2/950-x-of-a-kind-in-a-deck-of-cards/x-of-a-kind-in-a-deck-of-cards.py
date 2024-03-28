class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        di = Counter(deck)

        group_size = None
        for count in di.values():
            if group_size == None:
                group_size = count 
            else:
                group_size = gcd(group_size,count)
        
        return group_size >= 2

