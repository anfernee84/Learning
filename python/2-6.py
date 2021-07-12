def write_and_get_employees(employee_list, path):
    fh = open(path, 'w')
    for i in employee_list:
        for j in i:
            fh.write("%s\n" % j)   
    fh.close()
    fh = open(path, "r")
    symbols = []
    for line in fh:
        symbols.append(line.replace("\n",""))
    fh.close()
    return symbols
print(write_and_get_employees([['Robert Stivenson, 28', 'Alex Denver, 30'], ['Vasya Pupkin, 39']],'test.txt'))


# def write_and_get_employees(employee_list, path):
#     fh = open(path, 'w')
#     for el in employee_list:
#         for i in el:
#             fh.write(i + '\n')

#     fh.close()
#     fh = open(path, 'r')
#     lines = fh.readlines()
#     fh.close()
#     return lines