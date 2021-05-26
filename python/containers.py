"""
from typing import KeysView


nubbers = [1,5,3,6,8,5,3,1,2,]
letters = ["feg","fggh","rrh","rgerg"]
print(nubbers)
id = nubbers.index(8)
print (id)
ide = nubbers.index(3)
print (ide)
wah = nubbers.count(1)
nubbers.sort()
letters.sort(key=None, reverse=False)
print (nubbers)
print (letters)
nubbers.reverse()
print (nubbers)
letters = nubbers.copy()
print (letters)


dic = {"a" : 1, "b" : 2, "c" : 3}
slovar = dic.pop("c")
print(slovar)
dic.update({"c":3})
print(dic)
slovar = dic.copy()
dic.clear()
print (dic)
print (slovar)
slovar = dic.get("a",1)
#print (slovar)


digits = { 1: "one", 2: "two", 3: "three"}
for key in digits:
    print(key)

for val in digits.values():
    print(val)
for key, value in digits.items():
    print(key, value)

a = set("Privet")
print(a)
b = {3,5,6,7,4,8}
print(b)
b.add(35)
print (b)
b.remove(4)
print (b)
b.discard(8)
print (b)
c = set("hi , perverts")
print(a)
print(c)
print(a&c)
print (a^c)
print (a|c)
points = {
    (0, 0): "O",
    (1, 1): "A",
    (2, 2): "B"
}

tupl = (3,2,8,0)
#tupl[2] = "s"
s = "Privet dude"
print(s[-1])
print(s [3])
print(s.upper())
print(s.lower())
print(s.startswith("Pr"))
print (s.endswith('de'))
prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
is_pr = 3 in prime_numbers

user = {
    "name": "vasya",
    "surname" : "pupkin",
    "age" : 22
}
if "age" in user:
    print(f"User is {user['age']} years old")

password = input("enter password: ")
if len(password) < 8:
    print("password is too weak")

word = "rfbfgkskpfadbgnjaOASDVMKGF"
for letter in word:
    print (letter)

somewords = ["gthh", "ryhyhh", "rtgrh"]
for word in somewords:
    print(word)

oddnubbers = [1,3,5,7,9]
for nubber in oddnubbers:
    print(nubber ** 2)
    


"""
