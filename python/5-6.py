def get_ingredients(path, position_name):
    with open(path, 'r') as fh:
        while True:
            s = fh.readline()
            if position_name in s:
                end = s.rpartition(":")[-1]
                result = [s.strip() for s in end.split(',') if s.strip()]              
            elif not s:
                break
        return result




print (get_ingredients('test.txt', "Small chicken"))


# def get_ingredients(path, position_name):
#     with open(path, 'r') as fh:
#         while True:
#             s = fh.readline()
#             if position_name in s:
#                 result = (s.rstrip('\n').split(':'))[1].split(',')
#             elif not s:
#                 break
#         return result



    # with open(path, 'r') as fh:
    #     line = fh.readline()
    #     l = None
    #     if position_name in line:
    #         beg = line.partition(":")[0]
    #         print (beg)
    #         end = line.rpartition(":")[-1]
    #         print (end)
    #         l = c
    #     return l