"""
Connected Components of a graph via BFS

- All nodes are unexplored (assume labeled 1 to n)
- For i=1 to n:
    if i not yet explored:
        BFS(G, i)
"""
from collections import deque

# Graph with two connected components
graph = {
    1: [2],
    2: [1],
    3: [4],
    4: [3]
}

def bfs(graph, i):
    """Returns the set of all nodes explored starting from the node i in the input graph."""
    visited = set()

    unexplored = deque()
    unexplored.append(i)

    while unexplored:
        curr = unexplored.popleft()
        visited.add(curr)
        edges = graph[curr]

        for edge in edges:
            if edge in visited:
               continue
            else:
                unexplored.appendleft(edge)

    return visited


def connected_components(graph):
    """Returns the number of connected components in the graph."""
    all_nodes = list(graph.keys())

    counter = 0
    explored = set()
    components = []
    for node in all_nodes:
        if node not in explored:
            counter += 1
            visited = bfs(graph, node)
            components.append(visited)
            explored = explored.union(visited)

    return explored, components, counter

if __name__ == "__main__":
    all_explored, components, num_components = connected_components(graph)
    print(num_components, components)