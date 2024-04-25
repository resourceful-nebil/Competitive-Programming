class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        new_form = []
        for acc in accounts:
            name = acc[0]
            emails = set(acc[1:])
            new_form.append([name,emails])
        
        s = len(accounts)
        root = {i:i for i in range(s)}
        size = [1] * s
        
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        
        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if size[rootX] > size[rootY]:
                    root[rootY] = rootX
                    size[rootX] += size[rootY]
                else:
                    root[rootX] = rootY
                    size[rootY] += size[rootX]
        
        for i in range(s):
            for j in range(i):
                if new_form[i][0] == new_form[j][0]:
                    # print(new_form[i][1],new_form[j][1])
                    intersect = new_form[i][1].intersection(new_form[j][1])
                    # print(intersect)
                    if len(intersect) >= 1:
                        union(i,j)
        res = []
        for i,acc in enumerate(new_form):
            if find(i) != i:
                idx = find(i)
                new_form[idx][1] = new_form[idx][1].union(new_form[i][1])
        
        for i,acc in enumerate(new_form):
            if find(i) == i:
                name,email = acc
                sorted_email = sorted(email)
                res.append([name] + sorted_email)


        
        # print(new_form)
        return res