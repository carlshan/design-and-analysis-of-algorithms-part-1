# First I'm going to reverse the input graph and save it as an output
def read_directed_graph(filename):
    f = open(filename)

    adjlist = []
    adjlist_reversed = []

    line = f.readline()
    while line != '':
        num1, num2 = line.split()
        v_from = int(num1)
        v_to = int(num2)
        max_v = max(v_from, v_to)

        while len(adjlist) < max_v:
            adjlist.append([])
        while len(adjlist_reversed) < max_v:
            adjlist_reversed.append([])

        adjlist[v_from-1].append(v_to-1)
        adjlist_reversed[v_to-1].append(v_from-1)

        line = f.readline()

    return adjlist, adjlist_reversed


def get_graph(filename):
    adjlist, adjlist_reversed = read_directed_graph(filename)
    graph = {i: elem for i, elem in enumerate(adjlist)}
    reversed_graph = {i: elem for i, elem in enumerate(adjlist_reversed)}

    return graph, reversed_graph


def reverse_test_graph(graph):
    """Given an input directed graph, returns its reverse."""
    flatten = lambda l: [item for sublist in l for item in sublist] # flattens a list of lists
    nodes = set(graph.keys()).union(set(flatten(graph.values())))
    reversed_graph = {node: [] for node in nodes}

    for row in graph:
        outgoing_edges = graph[row]
        for edge in outgoing_edges:
            reversed_graph[edge].append(row)

    return reversed_graph