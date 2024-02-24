def find_double_promo(user_ID, promo_A_status, promo_B_status):

    result = []
    for i in range(len(user_ID)):
        user = user_ID[i]

        try:
            promo_a = promo_A_status[i]
        except KeyError:
            promo_a = 0

        try:
            promo_b = promo_B_status[i]
        except KeyError:
            promo_b = 0

        if promo_a == 1 and promo_b == 1:
            result.append(user)

    return result


user_ID = ['01', '02', '03', '04', '05', '06', '07']
promo_A_status = [1, 0, 0, 1, 1, 0, 1]
promo_B_status = [0, 0, 1, 1, 0, 1, 1]

double_ID = find_double_promo(user_ID, promo_A_status, promo_B_status)
print(double_ID)

# Expected ['04', '07']


user_ID = ['a', 'b', 'c', 'd', 'e']
promo_A_status = [1, 1, 1, 1, 1]
promo_B_status = [0, 1, 1, 1, 1]

double_ID = find_double_promo(user_ID, promo_A_status, promo_B_status)
print(double_ID)


# Expected ['b', 'c', 'd', 'e']


user_ID = ['a4a', '23b', 'f4c', '5d6']
promo_A_status = [0, 0, 1, 0]
promo_B_status = [0, 0, 1, 1]

double_ID = find_double_promo(user_ID, promo_A_status, promo_B_status)
print(double_ID)

# expected ['f4c']
