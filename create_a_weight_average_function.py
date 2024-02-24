def calc_weighted_avg(data, w):

    multiply_weights = []
    for i in range(len(data)):
        multiply_weight = data[i] * w[i]
        multiply_weights.append(multiply_weight)

    total_weight = sum(w)

    average_weight = sum(multiply_weights) / total_weight

    if average_weight < 0:
        return abs(round(average_weight, 0))
    else:
        return round(average_weight, 2)


data = [10, 20, 30, 40, 50]
w = [0.10, 0.20, 0.25, 0.3, 0.15]

avg = calc_weighted_avg(data, w)
print(avg)

# Expected 32.0


data = [-2, -1, 0, 1, 2]
w = [0.2, 0.2, 0.2, 0.2, 0.2]

avg = calc_weighted_avg(data, w)
print(avg)

# Expected 0.0


data = [12, 13.5, 9.8, 10.3]
w = [0.10, 0.20, 0.30, 0.40]

avg = calc_weighted_avg(data, w)
print(avg)

# Expected 10.96
