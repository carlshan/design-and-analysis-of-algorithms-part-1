"""
Download the following text file (right click and select "Save As..."): kargerMinCut.txt

The file contains the adjacency list representation of a simple undirected graph.
There are 200 vertices labeled 1 to 200. The first column in the file represents the vertex label,
and the particular row (other entries except the first column) tells all the vertices that the vertex is
adjacent to. So for example, the  6𝑡ℎ  row looks like : "6 155 56 52 120 ......". This just means that
the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,
120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it
on the above graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of
edge contractions. Initially, you might want to do this naively, creating a new graph from the old every
time there's an edge contraction. But you should also think about more efficient implementations.)

(WARNING: As per the video lectures, please make sure to run the algorithm many times with different
random seeds, and remember the smallest cut that you ever find.) Write your numeric answer in the space
provided. So e.g., if your answer is 5, just type 5 in the space provided.
"""
# Given the mathematical analysis of the Contraction Algorithm,
# I should run it 200^2 * log(200) ~ 21200 times to have a 199/200 chance of finding the minimum cut
import random
from tqdm import tqdm
import math

def get_graph():
    with open('./inputs/kargerMinCut.txt', 'r+') as input_file:
        data = input_file.readlines()
        data = list(map(lambda row: row.split(), data))
    return {row[0]: row[1:] for row in data}


def delete_edge(graph, clusters, debug):
    """
    Picks an edge and collapses those two into one side of the cut.

    TODO: Implement this more efficiently without having to also rely on a graph variable
    """
    start = -1
    tail = -1

    candidates = list(graph.keys())

    while start == tail or not edge_exists(graph, start, tail):

        start = random.choice(candidates)
        tail = random.choice(candidates)

    clusters[start].add(tail)
    clusters[start] = clusters[start].union(clusters[tail])
    del clusters[tail]

    if debug:
        print(start, tail)

    graph[start] += [
        elem for elem in graph[tail]
        if elem != start # deletes self-loops
    ]
    del graph[tail] # remove from the graph so this pair can't be chosen again


def calculate_crossing_edges(graph, clusters, debug):
    """
    Given the remaining list of two vertices (formed by many other vertices), count the number of crossing edges in
    between these two in the original graph.

    """
    keys = list(graph.keys())
    A = keys[0]
    B = keys[1]

    clusterA = clusters[A]
    clusterA.add(A)
    clusterB = clusters[B]
    clusterB.add(B)

    total_crosses = 0

    if debug:
        print("""The final graph is: {}
        The two clusters are:
        {}
        {}
        """.format(graph, clusterA, clusterB))

    for edge1 in graph[A]: # For every edge incident in the first
        if edge1 not in clusterA: # Checks if the edge points to the other "super" cluster
            total_crosses += 1

    return total_crosses

def min_cut(graph, debug=False):
    """
    Performs the min cut algorithm once:

    While there are more than two vertices left:
        1. Chooses an edge uniformly at random to delete.
        2. Delete self-loops

    Consider the two nodes that are left, and have them represent a "cut". Count the number of crossing edges.
    """

    clusters = {
        v: set() for v in graph.keys() # initializing as no vertices have been collapsed yet
    }

    while len(clusters) > 2: # until there are exactly two clusters left
        delete_edge(graph, clusters, debug)

    return calculate_crossing_edges(graph, clusters, debug)


def edge_exists(graph, start, tail):
    return tail in graph[start]


def run_trials(N):
    """
    Runs this algorithm a number of times to try to get the minimum cut.
    """
    curr_min = math.inf
    for _ in tqdm(range(N)):
        graph = get_graph()
        trial_min = min_cut(graph)
        if trial_min <= curr_min:
            curr_min = trial_min
    return curr_min

if __name__ == "__main__":
    graph = get_graph()
    n = len(graph)
    N = int(n**2 * math.log(n))
    # Running the below with N=N will virtually guarantee success ... but it takes forever.
    print(run_trials(1000))