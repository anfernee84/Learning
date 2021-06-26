string = "exclude from this [2354235] symbols it [    ,] vse"
# test = "this [strings groups] of symbols"
# start_index = test.find("[")
# end_index = test.find("]")
# print(start_index, end_index)
# new_string = test[:start_index] + test[end_index + 1:]
# print(new_string)


# def sanitize(data):
#     new_string = data[:]
#     while True:
#         start_index = new_string.find("[")
#         end_index = new_string.find("]") 
#         if start_index == -1:
#             break
#         new_string = new_string[:start_index] + new_string[end_index +1:]
#     return new_string

# print(sanitize(string))


# string = "ильс Бор родился в семье профессора физиологии Копенгагенского университета Христиана Бора (1858—1911)"
# def cound_digits(strinng):
#     count = 0
#     for el in string:
#         if el.isdigit():
#             count += 1

#     return count
# print (cound_digits(string))

# def cound_nunbers(strinng):
#     count = 0
#     pos = 0
#     while pos < len(string):
#         if string[pos].isdigit():
#             while string[pos].isdigit():
#                 pos += 1
#             count += 1
#         else:
#             pos == 1

#     return count
# print (cound_digits(string))

numbers = ["123", "456", "100", "13", "abc"]
def sanitize(data):
    result = []
    for el in data:
        if el.isdigit():
            result.append(el)
    return (result)
# sanitize_numbers = sanitize(numbers)
# print(sanitize_numbers)


def transform_to_int(data):
    result = []
    for el in data:
        result.append(int(el))
    return (result)


sanitize_numbers = sanitize(numbers)
sanitize_numbers = transform_to_int(sanitize_numbers)

sorted_sanitize_numbers = sorted(sanitize_numbers)

print(sanitize_numbers)
print (min(sanitize_numbers))
print (max(sanitize_numbers))
print(sum(sanitize_numbers) / len(sanitize_numbers))




