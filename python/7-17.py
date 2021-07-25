def encode(data):
    if not data:
        return []
    if data[0] == data[1]:
        count_str = data[0]
        quantity = 2
        main_list = [count_str, quantity]
        return main_list + encode(data[2:])
    else:
        count_str = data[0]
        return [count_str, 1] + encode(data[1:])

print(encode(["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]))