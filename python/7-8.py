def token_parser(s):
    if len(s) == 0:
        return []
    else:
        itog = []
        lex = ""
        for j in s.replace(' ', ''):
            if j not in ["+","-","*","/", "(", ")"]:
                lex += str(j)
            elif j in ["+","-","*","/", "(", ")"]:
                itog.append(lex)
                itog.append(str(j))
                lex = ''
        itog.append(lex)
    itog = [x for x in itog if x != '']
    return(itog)      



print(token_parser('(2+ 3) *4 - 5678 * 3'))


# def token_parser(s):
#     s1 = s.split()
#     s2 = []
#     for i in s1:
#         if len(i) > 1 and not i.isdigit():
#             for j in i:
#                 s2.append(j)
#         if len(i) == 1 or i.isdigit():
#             s2.append(i)
#     print(s2)   
#     return s2