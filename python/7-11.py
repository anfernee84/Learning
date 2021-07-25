def sequence_buttons(string):
    TRANSLIT_DICT = {
        "1": ['.', ',', '?', '!', ':'],
        "2": ["A", "B", "C"],
        "3": ["D", "E", "F"],
        "4": ["J", "H", "I"],
        "5": ["J", "K", "L"],
        "6": ["M", "N", "O"],
        "7": ["P", "Q", "R", "S"],
        "8": ["T", "U", "V"],
        "9": ["W", "X", "Y", "Z"],
        "0": [" "]}

    finalmessage = ""
    for i in string:
        for key, val in TRANSLIT_DICT.items():
            if i.upper() in val:
                ind = val.index(i.upper()) + 1
                finalmessage += (ind * key)
    return finalmessage
            




print (sequence_buttons("Hello dodik!"))