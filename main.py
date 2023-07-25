'''
Implementation of the local search method for solving knapsack problem.
'''
import numpy as np


def local_search(weights, values, capacity, init_solution):
    print("Initial Solution:", list(init_solution))
    size = len(weights)
    current_weight = init_solution.dot(weights)
    best_solution = init_solution
    best_fitness = 0
    if current_weight <= capacity:
        best_fitness = init_solution.dot(values)
    current_solution = init_solution.copy()
    flag = True
    while flag:
        flag = False
        for i in range(size):
            current_solution[i] = 1 - current_solution[i]
            current_weight = current_solution.dot(weights)
            current_fitness = 0
            if current_weight <= capacity:
                current_fitness = current_solution.dot(values)
            if current_fitness > best_fitness:
                best_solution = current_solution.copy()
                best_fitness = current_fitness
                flag = True
            current_solution[i] = 1 - current_solution[i]
        if flag:
            current_solution = best_solution.copy()
    print("Final Solution:", list(best_solution))
    print("Fitness:", best_fitness)


if __name__ == '__main__':
    weights = np.array([1, 2, 3, 2, 3, 4, 1, 5, 3])
    values = np.array([8, 11, 9, 12, 14, 10, 6, 7, 13])
    capacity = 16
    init_solutions = np.array([
        [0, 1, 1, 1, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 0, 1, 0]
    ])
    for init_solution in init_solutions:
        local_search(
            weights=weights,
            values=values,
            capacity=capacity,
            init_solution=init_solution
        )
