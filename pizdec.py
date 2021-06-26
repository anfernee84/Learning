phone_storage = ["0509298165", "380665442345", "504654764", "0000000000", "0677332142", "9876543210"]

"""
+380501234567 + 38 code country 050 code operator tel: 1234567
"""

codes_operator = {"039", "050", "063", "066", "067", "068", "073", "091"}

def is_valid_phone(phone):
    def is_valid_operator(phone):
        if len(phone) == 12:
        if phone[:2] == "38":
            return True
        else:
            return False
    if len(phone) == 10:
        if phone[:3] in codes_operator:
            return True
        else:
            return False
    
    return False

for phone in phone_storage:
    is_valid = is_valid_phone(phone)
    if is_valid:
        print("Phone {:>12} is valid".format(phone))
    
