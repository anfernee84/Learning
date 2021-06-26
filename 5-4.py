def lookup_key(data, value):
    result = []
    for i,j in data.items():
      if j == value:
#        print(i)
        result.append(i)
    return(result)


print(lookup_key({"Python": 1991, "Java": 1995, "JS": 1995}, 1995))
