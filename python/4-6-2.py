def add_employee_to_file(record, path):

    fh = open(path, "a")
    fh.write("%s\n" % record) 
    fh.close()


print(add_employee_to_file("Drake Mikelsson, 19", 'test.txt'))