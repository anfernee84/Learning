message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if 65 <= ord(ch) <= 90:
        encoded_message += chr((ord(ch) - 65 + offset) % 26 + 65)
    elif 97 <= ord(ch) <= 122:
        encoded_message += chr((ord(ch) - 97 + offset) % 26 + 97)
    else:
        encoded_message += ch
print(encoded_message) 
   


message = input('Введите сообщение: ')
offset = int(input('Введите сдвиг: '))
encoded_message = ''
for ch in message:
    ch = ord(ch)
    if (ch >= 65 and ch<=90) :
        ch = ch + offset
        while ch > 90 :
            ch = ch - 90 + 64
        ch = chr(ch)
        encoded_message = encoded_message + ch
    elif (ch >= 97 and ch <= 122) :
        ch = ch + offset
        while ch > 122 :
            ch = ch -  122 + 96
        ch = chr(ch)
        encoded_message = encoded_message + ch
    else:
        ch = chr(ch)
        encoded_message = encoded_message + ch
print(encoded_message)



#    if (ch.isupper()):
#        encoded_message += chr((ord(ch) + offset-65) % 26 + 65)
#    else:
#       encoded_message += chr((ord(ch) + offset - 97) % 26 + 97)
#print (encoded_message)



#    ch = ord(ch)
#    ch = ch + offset
#    ch = chr(ch)
#    encoded_message += ch
#print (encoded_message)