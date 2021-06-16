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


a = {1:2, 3:4, 5:6}
d = a
for i in a.copy():
    if i == 1:
        a.pop(1)
print(a)
print(d)
a.update ({9:9})

a = [1,2, 3,4]
d = a
for i in a.copy():
    if i == 1:
        a.pop(1)
print(a)
print(d)
'''
'''
print(a.popitem())

keys = [1,2,3]
values = [4,5,6]
#d = {l1[0]:l2[0],l1[1]:l2[1],l1[2]:l2[2]}
c = {}
for i,v in enumerate(keys):
    c[v] = values[i]
print(c)
'''

'''
d = {'math': 4, 'ukr': 5, 'phys' : 3, 'bio' : 4, 'geo' : 3}
marks = {1:0,2:0,3:0,4:0,5:0}
med = 0
c = 0
maxim = 0
for i in d.values():
    marks[i] += 1
print(marks)


for i in d.values():
    if i > maxim:
        maxim = i
    else:
        continue
print (maxim)

print(sum(d.values())/len(d))
print(max(d.values()))

marks = {i : 0 for i in range(1,6)}
print(marks)


keys = [1,2,3]
values = [4,5,6]
print(dict(zip(keys, values)))



s = {1,2,3}
l = [1,5,6,7,4,3,1,7,8,3,2,]
print(set(l))
#s = frozenset()
s2 = {1,4,5}
print(s&s2)
print(s^s2)
print(s|s2)
print(s - s2)

'''

d = {3:5, 6:2, 7:8, 9:0, 10:1}
min = {}
print (d)
print(sum(d.keys()))
print(sum(d.values()))
print(sum(d.values()) + sum(d.keys()))

for i in d.keys():
    if not i%2:
        print(i)

print (max(d.keys()))



