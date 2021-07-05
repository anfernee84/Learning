grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    count = 0
    new_list = []
    for i, j in students.items():
        for x, z in grade.items():
            if j == x:
                count += 1
                spisok = '{:>4}|{:<10}|{:^5}|{:^5}'.format (count, i, x, z)
                new_list.append(spisok)
    return new_list
            
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}

print(formatted_grades(students))
