import queue

def prim(graph):
    pq = queue.PriorityQueue()
    visited = set()
    start_vertex = list(graph.keys())[0]
    pq.put((0, start_vertex))
    mst = []
    while not pq.empty():
        weight, vertex = pq.get()
        if vertex in visited:
            continue

        visited.add(vertex)

        if vertex != start_vertex:  # Exclude the starting vertex
            mst.append((vertex, weight))

        # Add adjacent vertices to priority queue
        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                pq.put((edge_weight, neighbor))

    return mst

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 5), ('C', 7)],
    'B': [('A', 5), ('C', 9), ('D', 8)],
    'C': [('A', 7), ('B', 9), ('D', 6)],
    'D': [('B', 8), ('C', 6)]
}

minimum_spanning_tree = prim(graph)
print("Minimum Spanning Tree:", minimum_spanning_tree)
