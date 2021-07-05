import re


def find_word(text, word):
    d = {
    'result': None,
    'first_index': None,
    'last_index': None,
    'search_string': None,
    'string': None
    }
    if re.search(word, text):
        d['string'] = text
        result = re.search(word, text)
        d['search_string'] = result.group(0)  
        d['result'] = True
        if d['result'] == True:
            a = result.span()
            d['first_index'] = a[0]
            d['last_index'] = a[-1]
            return d
    else:
        d['string'] = text
        d['search_string'] = word
        d['result'] = False
    return d

  
print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Rossum"))

# def find_word(text, word):
#     result = re.search(word, text)
#     if result:
#         new_dict = {
#             'result': True,
#             'first_index': result.span()[0],
#             'last_index': result.span()[1],
#             'search_string': word,
#             'string': text

#         }
#     else:
#         new_dict = {
#             'result': False,
#             'first_index': None,
#             'last_index': None,
#             'search_string': word,
#             'string': text

#         }
#     return new_dict
