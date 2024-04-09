"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visited = set()
        total = 0

        def dfs(arr,i):
            # print(arr,i)
            nonlocal total

            total += employees[i].importance
            if arr:
                for j in range(len(arr)):
                    if arr[j] not in visited:
                        visited.add(arr[j])
                        i = idx[arr[j]]
                        dfs(employees[i].subordinates,i)



            # if employees[i].subordinates == []:
            #     return
            # for j in range(len(employees[i].subordinates)):
            #     if employees[i].subordinates[j] not in visited:
            #         visited.add(employees[i].subordinates[j])
            #         total += employees[employees[i].subordinates[j]].importance
            #         dfs(employees[i].subordinates[j])
        idx = defaultdict(int)
        for i in range(len(employees)):
            idx[employees[i].id] = i
        # print(idx)

        for i in range(len(employees)):
            if employees[i].id not in visited and employees[i].id == id:
                visited.add(employees[i].id)
                dfs(employees[i].subordinates,i)

        return total