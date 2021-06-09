'''
l = [1,2,3,4,5,"rthh", True]
l.append(["pizdec", 18])
l.extend(["pizdec", 18])
l.insert(2,9)
l.remove(5)
l.pop()
print (l)
'''
'''
a = []
for i in range(0,11,2):
    a.append(i)
print (a)
'''

'''
b = [i for i in range(0,11,) if i % 2 == 0]
print(b)

c = [i if not i % 2 else 0 for i in range(0,11,)]
print(c)
'''
'''
d = [0 if i%2 else 1 for i in range(10)]
print(d)

e = [0 if not i%2 else 1 for i in range(10)]
print(e)

f = [1 if i % 2 else 0 for i in range(10)]
print(f)

g = [i for i in range(10,0,-1)]
print(g)

s = input(": ")
j = [i for i in s if i not in "aeoyuiAEOYUI"]
print(j)
'''
'''
s = input(": ")
z = ['a','e','o','y','u','i','A','E','O','Y','U','I']
k = [i for i in s if i not in z]
print(k)
'''

'''
s = input(": ")
#z = ['a','e','o','y','u','i','A','E','O','Y','U','I']
k = [i for i in s if i not in "a,e,o,y,u,i,A,E,O,Y,U,I".split (" ")]
print(k)
'''

'''
l = [0]*10
print(l)
#l[3] = 2
#l[4] = 2
l[3:5] = [2,2]
s = "adcdefgj"
s1 = s[:3] + "aa" + s[5]
print(l)
print (s[2:6])
print (s1)
print (s[:-1])
'''
'''
c = (1,2)
print(c[1])
print(c[0])
c = list(c)
c.append(3)
c = tuple(c)
print(c)
'''
'''
c = [[11,1,1],2,3,4]
print (len(c))
print(len(c[0]))
'''



'''
answer = []
d = [[1, 2, 3, 6, 8], [4, 5, 6], [7 ,8 ,9]]
print (len(d[0]), len(d[1]), len(d[2]))

for i in d:
    print(len(i), end = " ")
print()


for i in d:
    s = 0
    for j in i:
        s+=j
    answer.append(s)
print (answer)    



for i in d:
    answer += [sum(i)]
print(answer)
'''


answer = []
c = [[1, 2, 3, 6, 8], [4, 5, 3, 6], [7 ,8 ,9]]
for i, val in enumerate(c):
    if 3 in val:
        answer += [i]
print(answer)
    



