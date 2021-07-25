def get_employees_by_profession(path, profession):
    with open(path, "r") as fh:
        l = fh.readlines()
        prof = []
        for i in l:
            if (i.find(profession) != -1):
                prof.append(i.replace("\n",""))
        st = "".join(prof)
        st = st.replace(profession, "")
        return(st.replace(" ", ""))



print(get_employees_by_profession("test.txt", "cook"))    



# def get_employees_by_profession(path, profession):
#     names = ''
#     with open(path, 'r') as file:
#         lines = file.readlines()
#         for item in lines:
#             name_prof = item.rstrip().split(' ')
#             if name_prof[1] == profession:
#                 names += name_prof[0]
#     return names