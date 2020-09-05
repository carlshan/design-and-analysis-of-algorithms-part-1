'''
Algorithms - design and analysis (Stanford), Part I.
Programming Question 4:
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714. Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second column is the head (recall the graph is directed, and the edges are directed from the first column vertex to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the vertex with label 2 has an outgoing edge to the vertex with label 47646
Your task is to code up the algorithm from the video lectures for computing strongly connected components (SCCs), and to run this algorithm on the given graph.
Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes, separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be 500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If your algorithm finds less than 5 SCCs, then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100, then your answer should be "400,300,100,0,0".
WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph you may have to manage memory carefully. The best way to do this depends on your programming language and environment, and we strongly suggest that you exchange tips for doing this on the discussion forums.
@author: Renat Alimbekov
'''

import sys
import threading

def readDirectedGraph(filename):
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


t = 0
s = None
explored = None
leader = None
scc_size = 0
sorted_by_finish_time = None

def DFS_Loop_1(graph_rev, n):

    global t, explored, sorted_by_finish_time

    t = 0
    explored = [False]*n
    sorted_by_finish_time = [None]*n

    for i in reversed(range(n)):
        if not explored[i]:
            DFS_1(graph_rev, i)


def DFS_1(graph_rev, i):

    global t, explored

    explored[i] = True

    for v in graph_rev[i]:
        if not explored[v]:
            DFS_1(graph_rev, v)

    sorted_by_finish_time[t] = i
    t += 1


def DFS_Loop_2(graph):

    global scc_size, explored, sorted_by_finish_time

    explored = [False]*len(graph)
    res = []

    for i in reversed(range(len(graph))):
        if not explored[sorted_by_finish_time[i]]:
            scc_size = 0
            DFS_2(graph, sorted_by_finish_time[i])
            res.append(scc_size)

    return res


def DFS_2(graph, i):

    global explored, scc_size

    explored[i] = True

    for v in graph[i]:
        if not explored[v]:
            DFS_2(graph, v)

    scc_size += 1


def kosarajuSCCsizes(graph, graph_rev):

    DFS_Loop_1(graph_rev, len(graph))
    res = DFS_Loop_2(graph)

    return res


def main():
    print('start')
    graph, graph_rev = readDirectedGraph('inputs/SCC.txt')
    print('start 1')
    res = kosarajuSCCsizes(graph, graph_rev)
    print('start 2')
    print(','.join(map(lambda x: str(x), sorted(res)[::-1][:5])))


if __name__ == '__main__':
    threading.stack_size(67108864)
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target = main)
    thread.start()