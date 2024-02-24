import math


def calc_dist_without_module(A, B):
    exponen_calc_1 = (A[0] - B[0]) ** 2
    exponen_calc_2 = (A[1] - B[1]) ** 2

    # square_root_1 = math.sqrt(exponen_calc_1)
    # square_root_2 = math.sqrt(exponen_calc_2)
    
    square_root_1 = exponen_calc_1 ** (1/2)
    square_root_2 = exponen_calc_2 ** (1/2)

    exponen_res_1 = square_root_1 ** 2
    exponen_res_2 = square_root_2 ** 2

    multipy_exponen_res = exponen_res_1 + exponen_res_2
    
    # return math.sqrt(multipy_exponen_res)
    return multipy_exponen_res ** (1/2)


def calc_dist(A, B):
    exponen_calc_1 = (A[0] - B[0]) ** 2
    exponen_calc_2 = (A[1] - B[1]) ** 2

    square_root_1 = math.sqrt(exponen_calc_1)
    square_root_2 = math.sqrt(exponen_calc_2)

    exponen_res_1 = square_root_1 ** 2
    exponen_res_2 = square_root_2 ** 2

    multipy_exponen_res = exponen_res_1 + exponen_res_2
    
    return math.sqrt(multipy_exponen_res)


def find_nearest(current_coor, tourism_coor, tourism_name):

    result = {}
    for i in range(len(tourism_name)):
        tourist_coor = tourism_coor[i]
        distance = calc_dist(current_coor, tourist_coor)

        name = tourism_name[i]
        if not result or (result.get('dist') and distance < result['dist']):
            result['object'] = name
            result['dist'] = distance

    return result


current_coor = [-2.21, 3.15]
tourism_coor = [
    [-34.93, -31.23],
    [-77.90, 79.90],
    [46.67, 40.44],
    [21.83, 1.94],
    [41.77, -63.44],
    [-1.10, -47.22],
    [68.81, 64.65],
    [-21.23, 22.03],
    [68.30, -69.73],
    [12.82, 30.75],
]
tourism_name = [
    'Pantai A',
    'Jembatan B',
    'Taman C',
    'Danau D',
    'Perpustakaan E',
    'Mall F',
    'Monumen G',
    'Taman Hutan H',
    'Air terjun I',
    'Gunung J'
]

nearest_object = find_nearest(current_coor, tourism_coor, tourism_name)
print(nearest_object)

# Expected {'object': 'Danau D', 'dist': 24.07043206924213}

current_coor = [0, 0]
tourism_coor = [
    [0, 1],
    [2, 0],
    [0, 3],
    [-1, -1],
    [-2, -1],
    [-1, -3]
]
tourism_name = [
    'object a',
    'object b',
    'object c',
    'object d',
    'object e',
    'object f'
]

nearest_object = find_nearest(current_coor, tourism_coor, tourism_name)
print(nearest_object)

# Expected {'object': 'object a', 'dist': 1.0}
