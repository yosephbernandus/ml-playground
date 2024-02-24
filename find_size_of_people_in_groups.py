def distribute_user(n, k):
    result = []

    size_group = n // k
    remaining_user = n % k
    for i in range(k):
        if i < remaining_user:
            result.append(size_group + 1)
        else:
            result.append(size_group)

    return result


n = 14
k = 3

group_size = distribute_user(n, k)
print(group_size)

# expected [5, 5, 4]


n = 40
k = 7

group_size = distribute_user(n, k)
print(group_size)

# expected [6, 6, 6, 6, 6, 5, 5]


n = 20
k = 2

group_size = distribute_user(n, k)
print(group_size)

# expected []