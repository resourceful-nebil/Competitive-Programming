class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
   
        path = defaultdict(list)
       
        for div in paths:
            divided = list(div.split())
            for i in range(1,len(divided)):
                data_type , content = divided[i].split("(")

                path[content].append(divided[0]+"/"+data_type)
        
        result = []

        for item in path.values():
            if len(item) >= 2:
                result.append(item)
        
        return result