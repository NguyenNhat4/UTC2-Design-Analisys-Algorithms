import heapq

def prim(graph):
    pq = []
    visited = set()
    start_vertex = list(graph.keys())[0]
    heapq.heappush(pq, (0, start_vertex))
    mst = []
    while pq:
        weight, vertex = heapq.heappop(pq)
        if vertex in visited:
            continue

        visited.add(vertex)

        if vertex != start_vertex:  
            mst.append((vertex, weight))

        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor))

    return mst

graph = {
    'A': [('B', 5), ('C', 7)],
    'B': [('A', 5), ('C', 9), ('D', 8)],
    'C': [('A', 7), ('B', 9), ('D', 6)],
    'D': [('B', 8), ('C', 6)]
}
minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
