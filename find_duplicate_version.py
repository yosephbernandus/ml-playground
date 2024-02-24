def find_duplicates(people_ID, people_name):
    result = []

    people_mapping_dicts = {}
    for i in range(len(people_name)):
        name = people_name[i]

        new_name = name.lower()
        if new_name not in people_mapping_dicts.keys():
            people_mapping_dicts[new_name] = [name]
        else:
            people_mapping_dicts[new_name].append(name)

    for i in range(len(people_ID)):
        id = people_ID[i]
        name = people_name[i]

        check_value = people_mapping_dicts.get(name.lower().strip())
        if check_value and len(check_value) > 1:
            result.append([id, name])

    return result


# def find_duplicates_multiple_loop(people_ID, people_name):
#     result = []

#     for i in range(len(people_ID)):
#         id = people_ID[i]
#         name = people_name[i]

#         is_exists = False
#         for j in range(i + 1, len(people_ID) -1):
#             if name.lower() == people_name[j].lower():
#                 is_exists = True

#         if is_exists:
#             result.append([id, name])

#     return result


people_ID = ['01', '02', '03', '04', '05', '06', '07']
people_name = [
    'Budi santoso',
    'Pramono Setiadi',
    'Rijal',
    'Dedi setiawan',
    'rijal',
    'Alesha Nur',
    'Dedi Setiawan'
]

people_duplicate = find_duplicates(people_ID, people_name)
print(people_duplicate)

# Expected [['03', 'Rijal'], ['04', 'Dedi setiawan'], ['05', 'rijal'], ['07', 'Dedi Setiawan']]


people_ID = ['1e', 'd2', '3b', 'a4', 'q5']
people_name = [
    'aa cahya',
    'AA cahYa',
    'bb durian',
    'cc maANGGa',
    'AA CAHYA ',
]

people_duplicate = find_duplicates(people_ID, people_name)
print(people_duplicate)

# Expected = [['1e', 'aa cahya'], ['d2', 'AA cahYa'], ['q5', 'AA CAHYA ']]