def all_sub_lists(data):


    lists = [[]]
    for i in range(len(data) + 1):
        for j in range(i):
            lists.append(data[j: i])
    lists.sort(key = len)
    return lists
 

l1 = [4, 6, 1, 3]
print(all_sub_lists(l1))


# Python program to print all
# sublist from a given list
 
# function to generate all the sub lists
# def sub_lists (l):
#     lists = [[]]
#     for i in range(len(l) + 1):
#         for j in range(i):
#             lists.append(l[j: i])
#     return lists
 
# # driver code
# l1 = [1, 2, 3]
# print(sub_lists(l1))