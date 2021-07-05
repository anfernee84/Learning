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
    sanphones = {"UA":"+380"}
    countrydict = {"JP":"+81", "SP":"+65", "TW":"+866", "UA":"+380"}
    for numb in list_phones:
        numb = sanitize_phone_number(numb)
        for i,j in countrydict.items():
            if j[1:] in numb[:3] and i not in sanphones:
                sanphones.update({i:[numb]})
            elif j[1:] in numb[:3] and i in sanphones.keys():
                sanphones[i].append(numb)
            elif j[1:] not in numb[:3] and "UA" not in sanphones.keys:
                sanphones.update({"UA":[numb]})
            elif j[1:] not in numb[:3] and "UA" in sanphones.keys:
                sanphones["UA"].append(numb)
                             

    return(sanphones)

print(get_phone_numbers_for_countries(["+380508509978", "+380509002254", "+390509002254"]))
