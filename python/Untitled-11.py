'''
s = input(":")
if "a" not in s:
   print ("No letter a") 
else:
    for i in range(len(s)):
        if s[i] == "a":
            print (i)
            break
'''
'''
s = input(":")
if "a" not in s:
   print ("No letter a") 
else:
    for i, val in enumerate(s):
        if val == "a":
            print (i)
            break
'''
'''
s = input(":")
for i,j in enumerate(s):
    print(f"{i}:{j}")
'''
'''
n = "12356"
sum = 0
sum = int(sum)
for i,j in enumerate(n):
    sum = sum + int(j)
print (sum)

'''
'''
n = int(input(": "))
n = abs(n)
sum = 0
while n:
    sum += (n % 10)
    n //= 10
print (sum)
'''
'''
n = int(input(": "))
n = abs(n)
ans = 0
while n:
    ans = ans * 10 + n%10
    n //= 10
print (ans)
'''
'''
n = int(input(": "))
while n:
    print (n)
    n-=1
'''
'''
login = "admin"
pwd = "root"
while True:
    a =  input ("Enter login: ")
    b =  input ("Enter password: ")
    if a != login or b != pwd:
        print ("L\p incorrect, try again?")
        c = input("1 - yes, 0 - no: ")
        if c == "0":
            break
        else:
            continue
    else:
        print ("L\p correct!")
    break
'''
'''
word = input(":")
count = 0
dig = 0
for i in word:
    if i in "aeiouAEIOU":
        count +=1
for c,f in enumerate(word):
    if f.isdigit():
        dig += 1
print (count)
print (dig)
'''
'''
word = int(input(":"))
a = 1
for i in range(1,word+1):
    a *= i
print (a)
'''
'''
word = int(input(":"))
a = 1
#n = None
while word:
    a = a * word
    word = word - 1
print (a)
'''


is_admin = bool(input("Пользователь администратор? "))
is_active = bool(input("Пользователь активен? "))
is_permission = bool(input("Пользователь имеет доступ? "))
if is_admin == True:
    access = True
    print ("ok")
elif is_active == True and is_permission == True:
    access = True
    print ("ok")
else:
    False
    print ("not ok")
