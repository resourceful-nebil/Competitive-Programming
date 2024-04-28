class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        distances = [0] * n
        subtree_sizes = [0] * n

        self.calculate_distances(graph, 0, distances, subtree_sizes, -1)

        self.calculate_sum_distances(graph, 0, distances, subtree_sizes, -1)

        return distances

    def calculate_distances(self, graph, node, distances, subtree_sizes, parent):
        subtree_sizes[node] = 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            self.calculate_distances(graph, neighbor, distances, subtree_sizes, node)
            subtree_sizes[node] += subtree_sizes[neighbor]
            distances[node] += distances[neighbor] + subtree_sizes[neighbor]

    def calculate_sum_distances(self, graph, node, distances, subtree_sizes, parent):
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            distances[neighbor] = distances[node] - subtree_sizes[neighbor] + (len(distances) - subtree_sizes[neighbor])
            self.calculate_sum_distances(graph, neighbor, distances, subtree_sizes, node)