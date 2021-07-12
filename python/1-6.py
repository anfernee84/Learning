def read_file(path):


    fh = open(path, 'r')
    sums = 0    
    while True:
        line = fh.readline()
        if not line:
            break
        l = line     
        l = l.rstrip("\n")
        l = l.split(" ")
        sums += float(l[1])
    fh.close()    
    return (sums)


print(read_file('test.txt'))