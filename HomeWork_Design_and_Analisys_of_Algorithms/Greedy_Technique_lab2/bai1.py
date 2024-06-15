import heapq

def prim_mst(distance_matrix):
    num_cities = len(distance_matrix)
    mst_edges = []
    visited = [False] * num_cities
    min_heap = [(0, 0, -1)] 
    while min_heap and len(mst_edges) < num_cities - 1:
        cost, to_city, from_city = heapq.heappop(min_heap)
        if visited[to_city]:
            continue
        visited[to_city] = True
        if from_city != -1:
            mst_edges.append((from_city, to_city, cost))

        for next_city in range(num_cities):
            if not visited[next_city]:
                heapq.heappush(min_heap, (distance_matrix[to_city][next_city], next_city, to_city))

    return mst_edges

def preorder_traversal(tree, start):
    visited = set()
    path = []

    def dfs(node):
        visited.add(node)
        path.append(node)
        for neighbor, _ in tree.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return path

def tsp_with_prim(distance_matrix, start_city):
    mst_edges = prim_mst(distance_matrix)
    tree = {}
    for from_city, to_city, cost in mst_edges:
        if from_city not in tree:
            tree[from_city] = []
        if to_city not in tree:
            tree[to_city] = []
        tree[from_city].append((to_city, cost))
        tree[to_city].append((from_city, cost))

    mst_path = preorder_traversal(tree, start_city)
    mst_path.append(start_city)  # Complete the cycle

    total_distance = 0
    for i in range(len(mst_path) - 1):
        total_distance += distance_matrix[mst_path[i]][mst_path[i+1]]

    return mst_path, total_distance

distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

start_city = 0 
path, total_distance = tsp_with_prim(distance_matrix, start_city)

print("Path:", path)
print("Total cost:", total_distance)
