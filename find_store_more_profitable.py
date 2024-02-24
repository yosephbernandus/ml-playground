def profitable_toko(toko_ID, revenues, costs):
    profitable_toko = []

    for i in range(len(toko_ID)):
        try:
            cost = costs[i]
        except KeyError:
            cost = 0

        try:
            revenue = revenues[i]
        except KeyError:
            revenue = 0

        if (revenue - cost) > 0:
            profitable_toko.append(toko_ID[i])

    return profitable_toko



toko_ID = ['A001', 'B002', 'C003', 'D004']
revenues = [80000, 120000, 57000, 450000]
costs = [90000, 110000, 57000, 420000]

toko_profit = profitable_toko(toko_ID, revenues, costs)
print(toko_profit)


# Expected ['B002', 'D004']


toko_ID = ['p', 'q', 'r']
revenues = [80, 90, 30]
costs = [70, 100, 20]

toko_profit = profitable_toko(toko_ID, revenues, costs)
print(toko_profit)

# Expected ['p', 'r']

toko_ID = ['a', 'b', 'c']
revenues = [80, 80, 70]
costs = [80, 80, 90]

toko_profit = profitable_toko(toko_ID, revenues, costs)
print(toko_profit)

# Expected []
