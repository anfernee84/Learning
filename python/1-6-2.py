def total_salary(path):

    fh = open(path, 'r')
    sums = 0    
    while True:
        line = fh.readline()
        if not line:
            break
        l = line     
        l = l.rstrip("\n")
        l = l.split(",")
        sums += float(l[1])
    fh.close()    
    return (sums)


print(total_salary('test.txt'))