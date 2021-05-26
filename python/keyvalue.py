def get_grade(key):
    grade = {"F" : 1, "FX" : 2, "E" : 3, "D" : 3, "C": 4, "B": 5, "A": 5}
    return grade.get(key)


def get_description(key):
    grades = {"F" : "неудовлетворительно", "FX" : "неудовлетворительно", "E" : "достаточно",
       "D" : "удовлетворительно", "C" : "хорошо", "B" : "очень хорошо",  "A" : "отлично" }  
    return grades.get(key)


mark = ("E")
point = ("C")
print (get_grade(mark))
print (get_description(point))
        
        
        