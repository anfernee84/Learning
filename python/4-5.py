def is_check_name(fullname, first_name):
    if fullname.find(first_name) != -1:
        return True
    else:
        return False



print(is_check_name("Pupkin Vasiliy Sidorovich", "Vasiliy"))


# j.find(key) != -1: