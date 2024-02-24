def check_structure(data):
    result = []
    total_rows = len(data)

    result.append(total_rows)
    for d in data:
        if len(d) in result:
            continue
        result.append(len(d))

    return result


def check_structure(data):
    result = []
    total_column = len(data)

    result.append(total_column)
    result.append(len(data[0]))

    return result


data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]]

res = check_structure(data)
print(res)

# Expected [4 3]

data = [[4, 3, 2, 10],
        [8, 2, 1, 3]]

res = check_structure(data)
print(res)

# Expected [2 4]

data = [[0.5, 0.3, 0.1]]

res = check_structure(data)
print(res)

# Expected [1 3]



# DO NOT CHANGE THE NAME & INPUT OF THE FUNCTION
def check_structure(data):
    '''
    Function to check the data structures

    Parameters
    ----------
    data : list
        The 2D sample data

    Returns
    --------
    data_shape : list
        The shape of data with format [nrows, ncols]
        nrows = number of rows
        ncols = number of columns
    '''
    
    result = []
    total_column = len(data)

    result.append(total_column)
    for d in data:
        if len(d) in result:
            continue
        result.append(len(d))

    return result
