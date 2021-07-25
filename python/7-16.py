def decode(data):
    if len(data) == 0:
        return []
    else:
        f = [data[0] * data[1]]
#        print (f)
        r = [i for i in f[0]]
#        print (r)
        f = r + decode(data[2:])
#        print (f)

        return f



print(decode(["X", 3, "Z", 2, "X", 6, "Y", 3, "Z", 2]))
