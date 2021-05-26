def prepare_data(data):
    data.remove(max(data))
    data.remove(min(data))
    sortarr = sorted(data)
    return(sortarr)

numbs = [1,5,8,4,5,3]
print (prepare_data(numbs))