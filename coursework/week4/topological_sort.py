"""
A topological ordering of a directed graph G is a labelling f of G's nodes such that:
    1. The f(v)'s are the set {1, 2, ..., n}
    2. (u, v) in G => f(u) < f(v)

It turns out that computing a topological ordering can be reduced to doing Depth-First Search.

Here's the algorithm:

DFS
- Mark all nodes unexplored
- current_label = n # too keep track of ordering
- for each vertex:
    - if v not yet explored:
        DFS(graph, v)

DFS(graph, s):
- mark s as explored
- for every edge (s, v):
    - if v not yet explored
    - DFS(G, v)
- set f(s) = current_label
- current_label -= 1

"""

graph = {
    's': ['v', 'w'],
    'v': ['t'],
    'w': ['t'],
    't': []
}

def topological_sort(graph):
    """
    Creates a topological ordering on a DAG.
    """

    explored = set()
    all_nodes = {node : None for node in graph}

    current_label = len(all_nodes)

    def dfs(graph, i):
        """Does recursive DFS on the input graph starting at node i."""
        nonlocal current_label

        explored.add(i)

        edges = graph[i]

        for edge in edges:
            if edge in explored:
                continue
            else:
                dfs(graph, edge)
        all_nodes[i] = current_label
        current_label -= 1

    for node in all_nodes:
        if node not in explored:
            dfs(graph, node)

    return all_nodes

if __name__ == "__main__":
    print(topological_sort(graph))