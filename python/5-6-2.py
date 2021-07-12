def get_cats_info(path):
    with open(path, 'r') as fh:
        result = []
        for string in fh:
            id, name, age = string.split(",")
            result.append({"id":id, "name":name, "age":age.strip()})
        return result
print(get_cats_info('test.txt'))

