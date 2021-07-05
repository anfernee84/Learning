import re

def find_all_words(text, word):
    result  = re.findall(word, text, re.IGNORECASE)
    return(result)




print(find_all_words("python PyThOn PYTHON PythoN piton pUthon", "python"))    