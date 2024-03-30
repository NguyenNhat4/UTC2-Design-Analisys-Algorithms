def calculate_distance(city1, city2):
    # Calculate Euclidean distance between two cities
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

def total_distance(path, cities):
    distance = 0
    for i in range(len(path) - 1):
        distance += calculate_distance(cities[path[i]], cities[path[i + 1]])
    distance += calculate_distance(cities[path[-1]], cities[path[0]])
    return distance

def permutations(arr):
    if len(arr) == 1:
        return [arr]
    perms = []
    for i in range(len(arr)):
        first = arr[i]
        rest = arr[:i] + arr[i + 1:]
        for perm in permutations(rest):
            perms.append([first] + perm)
    return perms

def exhaustive_search(cities):
    n = len(cities)
    # Generate all possible permutations of cities
    all_permutations = permutations(list(range(n)))
    min_distance = float('inf')
    best_path = None
    for path in all_permutations:
        distance = total_distance(path, cities)
        if distance < min_distance:
            min_distance = distance
            best_path = path
    return best_path, min_distance


cities = [(0, 0), (1, 2), (3, 1), (2, 3)] # coordinate of cities
best_path, min_distance = exhaustive_search(cities)
print("Best path:", best_path)
print("Minimum distance:", min_distance)

