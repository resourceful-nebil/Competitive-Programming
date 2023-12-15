class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        # used to store the last result wanted
        ans = []
        # used to store the number the count of visits for each domain
        visits = {}

        # splits the input string based on space and change the num to int
        for cp in cpdomains:
            num , domain = cp.split()
            num = int(num)
       
            # inserts domain as the key of the dictionary
            visits[domain] = visits.get(domain , 0) + num
            
            # splits the string after "."
            for i in range(len(domain)):
                if domain[i] == ".":
                    visits[domain[i+1:]] = visits.get(domain[i+1:] , 0) + num


        # appends strings to ans by iterating over visits hashmap
        for i in visits.keys():
            ans.append(f"{visits[i]} {i}")


        return ans