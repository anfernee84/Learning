def lookup_key(data,value):
    lis = []
    for i,x in data.items():
        if x == value:
            lis.append(i)
    print (lis)

lang = {"Python": 1991, "Java": 1995, "JS": 1995}
lookup_key(lang,1995)


def lookup_key(data, value):
    keys_list = list()
    for i in data.items():
        if i[1] == value:
            keys_list.append(i[0])
    return keys_list

lang = {"Python": 1991, "Java": 1995, "JS": 1995}
lookup_key(lang,1995)