def string_matching(full_string:str,sub_string:str)->int:
    #will return the first match index
    n = len(full_string)
    m = len(sub_string)
    for i in range(n-m+1):
        j = 0

        while j < m and full_string[i+j] == sub_string[j]:
            j+=1

        if (m == j):
            return i

    return -1




"""
The Traveling Salesperson Problem
I will not write code because it would be very difficult to understand.
Just focus on the analysis O(n!).
The same thing applies to the Knapsack Problem that it is O(2^n).
This is the most important thing about these two problems.
"""


############################################################################################
########################## A.I SLOP CODE ###################################################
############################################################################################
def knapsack_recursive(weights: list[int], values: list[int], capacity: int, n: int) -> int:
    if n == 0 or capacity == 0:
        return 0

    if weights[n-1] > capacity:
        return knapsack_recursive(weights, values, capacity, n-1)
    else:
        take_item = values[n-1] + knapsack_recursive(weights, values, capacity - weights[n-1], n-1)
        leave_item = knapsack_recursive(weights, values, capacity, n-1)
        return max(take_item, leave_item)

############################################################################################


############################################################################################
########################## A.I SLOP CODE ###################################################
############################################################################################
def get_permutations(cities: list[int]):
    if len(cities) <= 1:
        return [cities]
    perms = []
    for i in range(len(cities)):
        current = cities[i]
        remaining = cities[:i] + cities[i+1:]
        for p in get_permutations(remaining):
            perms.append([current] + p)
    return perms

def tsp_brute_force(matrix: list[list[int]]) -> int:
    n = len(matrix)
    cities = list(range(n))
    all_paths = get_permutations(cities)
    
    min_dist = float('inf')
    
    for path in all_paths:
        current_dist = 0
        for i in range(n - 1):
            current_dist += matrix[path[i]][path[i+1]]
        current_dist += matrix[path[-1]][path[0]]
        
        if current_dist < min_dist:
            min_dist = current_dist
            
    return min_dist
############################################################################################




def test_functions()->str:
    fullstr:str = "NABCDEFGHPLMOB"
    substr:str = "MOB"
    print(f"{fullstr} and {substr} are matching in index: {string_matching(fullstr,substr)}")
    print(f"{fullstr} and K are matching in index: {string_matching(fullstr,'K')}")
    print("="*40)
    
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5
    n = len(weights)

    result = knapsack_recursive(weights, values, capacity, n)
    print(f"Knapsack Max Value (Recursive): {result}")
    print("="*40)

    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    print(f"TSP Min Distance: {tsp_brute_force(dist_matrix)}")

    return ""

if (__name__ == "__main__"):
    test_functions()