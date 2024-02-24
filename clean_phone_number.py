def clean_phone_number(phone_list):
    cleaned_phone_number = []
    for phone in phone_list:
        phone = phone.replace(' ', '').replace('-', '')

        if phone.startswith('+628'):
            phone = phone.replace('+628', '628')
        elif phone.startswith('08'):
            phone = phone.replace('08', '628')
        else:
            phone = f'62{phone}'

        if len(phone.split('62')[1]) < 11:
            phone = 'Invalid number'
        else:
            phone = int(phone)
            

        cleaned_phone_number.append(phone)

    return cleaned_phone_number


phone_lists = [
    '82123321123',
    '082321123321',
    '+6282-456-654-456',
    '+62 82 789 987 789',
    '14045',
    '82145-451-145'
]

phone_clean = clean_phone_number(phone_lists)
print(phone_clean)

# Expected [6282123321123, 6282321123321, 6282456654456, 6282789987789, 'Invalid number', 6282145451145]


phone_lists = [
    '82432234432',
    '+62 82 32',
    '14032',
    '082 234 432 234'
]

phone_clean = clean_phone_number(phone_lists)
print(phone_clean)


# Expected [6282432234432, 'Invalid number', 'Invalid number', 6282234432234]
