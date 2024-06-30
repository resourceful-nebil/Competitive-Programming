class UnionFind:
    def __init__(self, size):
        # Initializes the UnionFind structure.
        # Each node is its own parent at first, and the size of each set is 1.
        # `count` tracks the number of disjoint sets.
        self.parent = list(range(size))
        self.set_size = [1] * size
        self.count = size

    def find(self, node):
        # Recursively finds the root parent of a node.
        # Applies path compression by linking the node directly to the root parent.
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        # Merges the sets of node1 and node2.
        # If they already share the same parent, no union is performed, returns False.
        # Otherwise, the smaller set is merged into the larger one, and True is returned.
        root1, root2 = self.find(node1 - 1), self.find(node2 - 1)
        if root1 == root2:
            return False
        if self.set_size[root1] > self.set_size[root2]:
            self.parent[root2] = root1
            self.set_size[root1] += self.set_size[root2]
        else:
            self.parent[root1] = root2
            self.set_size[root2] += self.set_size[root1]
        self.count -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, num_nodes: int, edges: List[List[int]]) -> int:
        # Initializes two UnionFind instances, one for Alice and one for Bob.
        alice_union_find = UnionFind(num_nodes)
        bob_union_find = UnionFind(num_nodes)
        num_edges_removed = 0

        # Adds type 3 edges (common to both Alice and Bob).
        # If an edge cannot be added because it does not merge two different sets,
        # it is considered redundant and can be removed.
        for edge_type, node1, node2 in edges:
            if edge_type == 3:
                if not alice_union_find.union(node1, node2):
                    num_edges_removed += 1
                else:
                    # Add the edge for Bob as well since it's a common edge.
                    bob_union_find.union(node1, node2)

        # Adds type 1 and type 2 edges (specific to Alice and Bob respectively).
        # If an edge cannot be added because it does not merge two different sets,
        # it is considered redundant and can be removed.
        for edge_type, node1, node2 in edges:
            if edge_type == 1:
                # If the edge cannot be added, increment the removal count.
                if not alice_union_find.union(node1, node2):
                    num_edges_removed += 1
            elif edge_type == 2:
                if not bob_union_find.union(node1, node2):
                    num_edges_removed += 1

        # The graph is fully connected for both Alice and Bob only if both have exactly one set.
        # In such a case, return the number of edges removed, otherwise return -1.
        if alice_union_find.count == 1 and bob_union_find.count == 1:
            return num_edges_removed
        else:
            return -1
