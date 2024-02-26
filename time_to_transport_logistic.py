def calculate_duration(route, duration_table):
    rows_value = {}

    column = list(set(route))
    column.sort()
    for i in range(len(column)):

        rows_value[column[i]] = {}
        for j in range(len(column)):
            rows_value[column[i]][column[j]] = duration_table[i][j]

    list_of_time = []
    for i in range(len(route)):
        next_index = (i + 1) % len(route)
        values = rows_value[route[i]][route[next_index]]
        list_of_time.append(values)

    return sum(list_of_time)


def calculate_duration(route, duration_table):
    total_time = 0
    for i in range(len(route) - 1):
        start = ord(route[i]) - ord('A')
        end = ord(route[i + 1]) - ord('A')
        total_time += duration_table[start][end]
    # Add the time to return to the initial position
    start = ord(route[-1]) - ord('A')
    end = ord(route[0]) - ord('A')
    total_time += duration_table[start][end]
    return total_time



duration_table = [
    [0, 3, 5, 10, 4],
    [3, 0, 6, 8, 9],
    [5, 6, 0, 7, 2],
    [10, 8, 7, 0, 1],
    [4, 9, 2, 1, 0]
]
route = 'ABCDEBE'

total_time = calculate_duration(route, duration_table)
print(total_time)

# Expected 39, beacuse after last iteration E should be back to A = 39

duration_table = [
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
]
route = 'ABCDCDBAB'

total_time = calculate_duration(route, duration_table)
print(total_time)


# # Expected 31

# #Example =
# [
#     [0, 3, 5, 10, 4],
#     [3, 0, 6, 8, 9],
#     [5, 6, 0, 7, 2],
#     [10, 8, 7, 0, 1],
#     [4, 9, 2, 1, 0],
# ]

# ABCDEBEA

# 3 + 6 + 7 + 1 + 9 + 9 + 4
# AB + BC + CD + DE + EB + BE + EA

1 + 4 + 6 + 6 + 6 + 1 + 1