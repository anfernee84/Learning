def file_operations(path, additional_info, start_pos, count_chars):
    with open (path, "a") as fh:
        fh.write(additional_info)
    with open (path, "r") as fh:
        fh.seek(start_pos)
        s = fh.read(count_chars)


    return(s)









print(file_operations("test.txt", "sgthsrtjsrjwrthw", 5, 3))
