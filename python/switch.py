num = input('Enter digit ')
def switch_case(case):
    return "You entered " + {
    '1' : "one",
    '2' : "two",
    '3' : "three"
    }.get(case, "an out of range number") 
print (switch_case(num))