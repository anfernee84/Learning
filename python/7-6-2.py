def sanitize_file(source, output):
    with open(source, 'r') as fh:
        strings = fh.readlines()
        newline = ""
        for i in strings:
            for j in i:
                if j.isdigit():
                    continue
                else:
                    newline += j
    with open(output, "w") as fu:
        fu.write(newline)
       

    






print(sanitize_file("test.txt", "test2.txt"))