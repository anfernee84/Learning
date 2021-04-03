def get_fullname(first_name, last_name, middle_name = "" ):
    return(str(first_name + middle_name + last_name))


print (get_fullname("Vasya ","Pupkin"))
print (get_fullname("Grisha ", "Smirnov", middle_name = "Sidorovich "))