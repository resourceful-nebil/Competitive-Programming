class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.set_size = [1] * (size + 1)
        self.count = size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
            node = self.parent[node]
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return 0
        if self.set_size[root1] > self.set_size[root2]:
            self.parent[root2] = root1
            self.set_size[root1] += self.set_size[root2]
        else:
            self.parent[root1] = root2
            self.set_size[root2] += self.set_size[root1]
        self.count -= 1
        return 1
    def isConnected(self):
        return self.count == 1


class Solution:
    def maxNumEdgesToRemove(self, num_nodes: int, edges: List[List[int]]) -> int:
        alice = UnionFind(num_nodes)
        bob = UnionFind(num_nodes)
        cnt = 0

        for edge_type, node1, node2 in edges:
            if edge_type == 3:
                cnt += (alice.union(node1,node2) | bob.union(node1,node2))
                
                

        for edge_type, node1, node2 in edges:
            if edge_type == 1:
                cnt += alice.union(node1,node2)
            elif edge_type == 2:
                cnt += bob.union(node1,node2)   

        if alice.isConnected() and bob.isConnected():
            return len(edges) - cnt
        else:
            return -1
