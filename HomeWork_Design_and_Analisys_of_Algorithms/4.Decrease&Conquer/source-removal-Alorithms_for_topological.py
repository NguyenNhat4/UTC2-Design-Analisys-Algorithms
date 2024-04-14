from collections import deque

def topological_sort(vertices, edges):
    in_degree = {u: 0 for u in vertices}
    graph = {u: [] for u in vertices}
    

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1
    
 
    queue = deque([u for u in vertices if in_degree[u] == 0])
    
    top_order = []
    
    while queue:
        u = queue.popleft()
        top_order.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(top_order) == len(vertices):
        return top_order
    else:
        return None

# Example usage:
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
print(topological_sort(vertices, edges))
