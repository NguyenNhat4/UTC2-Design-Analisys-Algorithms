import matplotlib.pyplot as plt
import numpy as np

# Brute-Force Polynomial Evaluation
def brute_force_polynomial_evaluation(poly, x):
    result = 0
    count_assignments = 0
    n = len(poly)
    for i in range(n):
        term = 1
        for j in range(i):
            term *= x
            count_assignments += 1
        result += poly[i] * term
        count_assignments += 1
    return count_assignments

# Improved Polynomial Evaluation
def polynomial_evaluation_improved(poly, x):
    result = 0
    count_assignments = 0
    n = len(poly)
    for i in range(n-1, -1, -1):
        count_assignments += 1
        result = result * x + poly[i]
        count_assignments += 1
    return count_assignments

# Generate random polynomial coefficients
def generate_random_polynomial(n):
    return np.random.randint(1, 100, n)

# Compare algorithms for given n
def compare_algorithms(n):
    poly = generate_random_polynomial(n)
    x = 2
    assignments_brute_force = brute_force_polynomial_evaluation(poly, x)
    assignments_improved = polynomial_evaluation_improved(poly, x)
    return assignments_brute_force, assignments_improved

# Values of n
ns = np.arange(100, 3000, 100)  # from 100 to 10000 with step 100

# Calculate assignments for each value of n
assignments_brute_force_list = []
assignments_improved_list = []

for n in ns:
    assignments_brute_force, assignments_improved = compare_algorithms(n)
    assignments_brute_force_list.append(assignments_brute_force)
    assignments_improved_list.append(assignments_improved)

# Plotting
plt.plot(ns, assignments_brute_force_list, marker='o', label='Brute-Force Polynomial Evaluation')
plt.plot(ns, assignments_improved_list, marker='o', label='Improved Polynomial Evaluation')
plt.title('Comparison of Assignments')
plt.xlabel('n')
plt.ylabel('Number of Assignments')
plt.xscale('log')  # Set logarithmic scale for x-axis
plt.yscale('log')  # Set logarithmic scale for y-axis
plt.legend()
plt.grid(True)
plt.show()

