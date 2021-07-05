def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    phone_dict = {'JP':[], 'SG':[], 'TW':[], "UA":[]}
    for i in list_phones:
        sannumber = sanitize_phone_number(i)
        if sannumber.startswith('380'):
            phone_dict['UA'].append(sannumber)
        elif sannumber.startswith('81'):
            phone_dict['JP'].append(sannumber)
        elif sannumber.startswith("65"):
            phone_dict['SG'].append(sannumber)
        elif sannumber.startswith('886'):
            phone_dict['TW'].append(sannumber)
        else:
            phone_dict['UA'].append(sannumber)
    return(phone_dict)

print(get_phone_numbers_for_countries(["+380508509978", "+380509002254", "+886509002254", "+444509002254"]))
