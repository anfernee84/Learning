#простонародный вариант
def real_len(text):
    text = text.replace("\n", "").replace("\f", "").replace("\r", "").replace("\t", "").replace("\v", "")
    return(len(text))

print(real_len("ehrhe\ndgjghhggh\vhrdth\tdrhred\f"))

#вариант с регуляркой





