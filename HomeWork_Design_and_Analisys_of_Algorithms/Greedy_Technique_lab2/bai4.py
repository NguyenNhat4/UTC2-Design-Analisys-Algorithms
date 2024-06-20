import heapq

def greedy_tsp(distance_matrix):
    """Finds an approximate solution to the TSP using a greedy approach.

    Args:
        distance_matrix: A list of lists representing the distances between cities.

    Returns:
        A tuple containing:
            - The tour as a list of city indices (starting and ending at 0).
            - The total distance of the tour.
    """

    num_cities = len(distance_matrix)
    unvisited = set(range(1,num_cities))
    current_city = 0
    tour = [current_city]
    total_distance = 0

    while unvisited:
        nearest_city = -1
        min_distance = float("inf")
        for city in unvisited:
            if city >= len(distance_matrix[current_city]):
                distance =  distance_matrix[city][current_city]
            else:
                distance = distance_matrix[current_city][city]
            if distance < min_distance:
                min_distance = distance
                nearest_city = city

        total_distance += min_distance
        unvisited.remove(nearest_city)
        tour.append(nearest_city)
        current_city = nearest_city

    # Return to the starting city
    total_distance += distance_matrix[current_city][0]
    tour.append(0)
    return tour, total_distance


# Example usage
distance_matrix = [
    [],
    [15],
    [12, 6],
    [6, 23, 16],
    [4, 5, 13, 26],
    [8, 4, 10, 14, 24],
    [11, 1, 2, 9, 5, 7]
]

tour, total_distance = greedy_tsp(distance_matrix)

# Convert city indices to letters (assuming a, b, c, ...)
city_names = "abcdefg"
tour_names = [city_names[i] for i in tour]

print("Tour:", tour_names)
print("Total distance:", total_distance)
