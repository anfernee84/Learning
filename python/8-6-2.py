def save_applicant_data(source, output):
    with open(output, 'w') as fh:
        st = ""
        for elem in source:
            for i,j in elem.items():
#                print(j)
                st += str(j) + ","
            st = st[:-1]   
            st += "\n"
            
        fh.write(st)
#            fh.write(st)







source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]


save_applicant_data(source, "test2.txt")