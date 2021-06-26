def split_list(grade):
    less = []
    more = []
    total = []
    if grade == []:
        return (less, more)
    else:
        mid = sum(grade) / len(grade) 
        for i in grade:
          if i <= mid:
            less.append(i)
          elif i > mid:
            more.append(i)
#        less.sort()
#        more.sort()
        total.append(sorted(less))
        total.append(sorted(more))
#        total = tuple(total)
        return(tuple(total))

print(split_list([2,6,7,4,5,2,9,6,4,3]))
