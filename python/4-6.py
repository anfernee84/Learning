def navigate_clients(path, code):

    fh = open(path, "r")
 #   line = fh.readline()
    fh.seek(len(code) + 1)
    second = fh.readline()
    fh.close()
    return second

print(navigate_clients("test.txt", "7777777"))

