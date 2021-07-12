def add_order(order, path):


    fh = open(path, "a")
    fh.write("%s\n" % order) 
    fh.close()
    fu = open(path, "r")
    activeorders = []
    for line in fu:        
        string = line.rpartition(":")[-1]
        if string == "active\n":
            activeorders.append(line)
    fu.close()
    return(len(activeorders))



print(add_order("Big goose:active", 'test.txt'))