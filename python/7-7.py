def data_preparation(list_data):
    itog = []
    for lst in list_data:
        if len(lst) > 2:
            lst.remove(max(lst))
            lst.remove(min(lst))
            itog.extend(lst)
        else:
            itog.extend(lst)
    itog.sort()
    itog.reverse()
    return (itog)
    


print(data_preparation([[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]))
