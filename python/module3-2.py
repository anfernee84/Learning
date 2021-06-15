import collections
from typing import Counter
'''
a = {}
a["Hello"] = "world"
print(a)

a[1] = 2
print(a)

a["qwerty"] = 5
print(a)

a[(1,2)] = 8
print (a)

a[2] = [4,5]
print(a)

a[1] = 5 
print(a)
print(a[2])
print(a.get(1, "error"))
print(list(a.keys()))
print(list(a.values()))

for i in a.keys():
    print(i, end = ",")
print("\n<---------------->")

for i in a.values():
    print (i)

for k,v in a.items():
    print (k, ":", v)

z = {1:2, 2:3, 3:2, 4:2}
sum = 0
for k,v in z.items():
    if k == 2:
        sum +=1
    if v == 2:
        sum+=1
print(sum)


s = list("Hello")
d = {}
for i in s:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)

d1 = Counter(s)
print(dict(d1))

d2 = collections.defaultdict(int)
for i in s: 
    d2[i] += 1
print(dict(d2))
'''

a = {1:2, 3:4}
d = a
for i in a.copy():
    if i == 1:
        d.pop
print(a)

