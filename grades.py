def get_grade(key):
    dict1 = {"F" : 1, "FX" : 2, "E" : 3, "D" : 3, "C" : 4, "B" : 5, "A" : 5}
    if key in dict1.keys():
        return(dict1[key])
    else:
        return(None)
#    for k in dict1.keys():
#        if k == key:
#            return(dict1[key])

def get_description(key):
    dict2 = {"F" : "неудовлетворительно", "FX" : "неудовлетворительно", "E" : "достаточно", "D" : "удовлетворительно", "C" : "хорошо", "B" : "очень хорошо", "A" : "отлично"}
    for k in dict2.keys():
        if k == key:
            return(dict2[key])



print(get_grade("A"))
print(get_description("A"))