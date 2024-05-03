
# DFS & BFS

import random

def bfs(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return visited
    current = queue.pop(0)
    visited.add(current)
    print(current,end=" ")
    for neighbor in graph[current] - visited:
        queue.append(neighbor)
    return bfs(graph, queue, visited)
 

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start,end=" ")
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

def create_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes : "))
    for node in range(num_nodes):
        graph[str(node)] = set()
    num_edges = int(input("Enter the number of edges : "))
    for _ in range(num_edges):
        edge = input("Enter edge (format: node1 node2) : ").split()
        node1, node2 = edge
        graph[node1].add(node2)
        graph[node2].add(node1)
    return graph

graph = create_graph()

start_node = input("Enter Starting Node : ")
queue = [start_node]

print("\nDFS of the given graph : ")
dfs(graph,start_node)

print("\n\nBFS of the given graph : ",)
bfs(graph,queue)
