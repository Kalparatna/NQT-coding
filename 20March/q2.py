'''
Problem Statement
You are given a Directed Acyclic Graph (DAG) with N vertices and M edges. Each edge has a
weight associated with it. Your task is to find the shortest path from a given source node (SRC)
to a destination node (DES) using the provided graph data.
Input Format
1.N M — Two integers representing the number of vertices (N) and the number of edges (M).
X Y W — Three integers for each edge representing an edge from vertex X to vertex Y with
weight W.
2.
SRC DES — Two integers representing the source node (SRC) and the destination node
(DES).
3.
Output Format
Print the shortest path from SRC to DES.
Display the total weight of this path.
Example Input
3 3
0 1 5
1 2 3
0 2 10
0 2
Example Output
Path: 0 -> 1 -> 2, Total Weight: 8


'''
from collections import defaultdict

def dfs(graph, current, dest, visited, path, weight, result):
    if current == dest:
        if weight < result["min_weight"]:
            result["min_weight"] = weight
            result["best_path"] = list(path)
        return

    for neighbor, w in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            path.append(neighbor)
            dfs(graph, neighbor, dest, visited, path, weight + w, result)
            path.pop()
            visited.remove(neighbor)

def find_shortest_path_dfs_only(N, M, edges, SRC, DES):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))

    visited = set()
    visited.add(SRC)
    path = [SRC]
    result = {
        "min_weight": float('inf'),
        "best_path": []
    }

    dfs(graph, SRC, DES, visited, path, 0, result)

    if result["min_weight"] == float('inf'):
        return "No path found"

    path_str = ' -> '.join(map(str, result["best_path"]))
    return f"Path: {path_str}, Total Weight: {result['min_weight']}"
    
if __name__ == "__main__":
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    SRC, DES = map(int, input().split())

    output = find_shortest_path_dfs_only(N, M, edges, SRC, DES)
    print(output)
