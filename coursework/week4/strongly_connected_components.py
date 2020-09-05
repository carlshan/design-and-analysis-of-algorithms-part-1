"""
A strongly connected component in a directed graph is one in which any vertex in this collection can be reached
from any other vertex in the collection.
"""
from util import get_graph, reverse_test_graph
import sys
from collections import defaultdict
import threading



def scc(graph, order=None):
    """
    This function is equivalent to DFS-Loop in the video.
    Video link: https://www.youtube.com/watch?v=O98hLTYVN3c
    (See 17:32)

    Parameters:
        graph (list)
            Adjascency list representation of a graph.
        order (list)
            An optional ordered list of nodes that the graph should be traversed in.

    Return:
        all_nodes (dict)
            Dictionary with finishing times for each node.
        leaders (dict)
            Dictionary with each node and the final SCC label they are given.
    """

    # Initializing key variables
    explored = set()
    flatten = lambda l: [item for sublist in l for item in sublist] # helper function that flattens a list of lists
    nodes = set(graph.keys()).union(set(flatten(graph.values()))) # There are some nodes without any outgoing edges so we need to take all the ones with incoming and outgoing edges

    all_nodes = {node: None for node in nodes}
    time = 0 # For finishing times in first pass
    leaders = {node: None for node in nodes} # For tracking how nodes are grouped together as an SCC in the second pass

    def dfs(graph, node, leader, leaders):
        """Does recursive DFS on the input graph starting at the input node."""
        nonlocal time

        if node not in graph:
            return

        explored.add(node) # mark node as explored
        leaders[node] = leader

        for edge in graph[node]:
            if edge not in explored:
                dfs(graph, edge, leader, leaders)

        time += 1
        all_nodes[node] = time

    if order: # Used in second pass: traverse in the order of decreasing times
        ordering = order
    else: # First pass: traverse the nodes in descending order of their node label
        ordering = sorted([node for node in nodes], reverse=True)

    for node in ordering:
        if node not in explored:
            leader = node
            dfs(graph, node, leader, leaders)

    return all_nodes, leaders


def kosaraju(graph, reversed_graph):
    """
    Kosaraju's algorithm computes strong-connected components in O(m+n) time.
    Runs Kosaraju's Two-Pass algorithm, described below:

    1. Let g_rev be the reversed graph.
    2. Run DFS-Loop on g_rev
    3. Run DFS-Loop on the original graph

    Returns:
        times: dict
        leader: dict
    """

    # First pass on the reversed graph.
    times, leader = scc(reversed_graph) # the first time leader is returned it should not be useful since it's on the reversed graph

    times = sorted(times.items(), key=lambda pair: pair[1], reverse=True) # Getting the keys in decreasing order of processing time
    times = [pair[0] for pair in times] # Just getting node in the order we want to process them

    # Second pass on the original graph with the correct order
    times, leader = scc(graph, order = times)

    # Now we know all the leaders and can figure out the SCCs
    return times, leader


def get_sccs(grouped):
    """
    Creates a dictionary of each node and its SCC label.
    """
    groups = defaultdict(lambda: [])
    for node in grouped:
        label = grouped[node]
        groups[label].append(node)

    return groups

def get_group_sizes(groups):
    """Returns a list containing the size of each SCC group from largest to smallest."""
    sizes = sorted([len(groups[label]) for label in groups], reverse=True)
    return list(sizes)


def main(filename, test=False):
    # Sets up in the inputs
    # This test graph is from the "Computing Strong Components: The Algorithm" video
    # 7, 3, 1, 8, 2, 5, 9, 4, 6 are one possible set of finishing times for the nodes 1...9.
    test_graph = {
        1: [7],
        2: [5],
        3: [9],
        4: [1],
        5: [8],
        6: [3, 8],
        7: [4, 9],
        8: [2],
        9: [6]
    }

    if test: # Used for testing
        graph = test_graph
        reversed_graph = reverse_test_graph(graph, test=test)
    else:
        graph, reversed_graph = get_graph(filename)
    times, leader = kosaraju(graph, reversed_graph)

    # Print results
    sccs = get_sccs(leader)
    sizes = [len(sccs[scc]) for scc in sccs]
    answers = sorted(sizes, reverse=True)

    for answer in answers[:5]: # Print the five largest SCCs
       print(answer)

if __name__ == "__main__":
    FILENAME = 'inputs/SCC.txt'
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target = main, args = (FILENAME, False, ))
    thread.start()
