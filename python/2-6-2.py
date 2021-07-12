def write_employees_to_file(employee_list, path):
    fh = open(path, 'w')
    for i in employee_list:
        for j in i:
            fh.write("%s\n" % j)   
    fh.close()
