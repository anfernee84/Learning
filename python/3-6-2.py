def read_employees_from_file(path):
    fh = open(path, "r")
    symbols = []
    for line in fh:
        symbols.append(line.replace("\n",""))
    fh.close()
    return symbols