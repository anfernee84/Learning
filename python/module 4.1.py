'''
def func(a,b):
    print("hello world")
    print(f"a:{a}, b:{b}")
    return 5
a = func(2,3)
func(4,5)
func(6,3)
print(a)
'''
'''
def calc(a,b,c):
    if c == "+":
        return (a+b)
    elif c == "-":
        return (a-b)
    elif c == "*":
        return (a*b)
    elif c == "/":
        return (a/b)

print(calc (5,3,"-"))




def sumlist(a):
    s = 0
    for i in a:
        s+=i
    return(s)
a = [1,2,3,4]
print(sumlist(a))


def list_sum():
    print(l)
    l.append(3)
    print(l)
l = [1,2,3]
list_sum()


def list_sum():
    global l
    print(l)
    l+=3
l = 3
print(l)

def funco(a,b):
    return(a+b)


a = 1
b = 2
print(funco(a,b))

def func (a, b=5, c=7):
    print(a,b,c)
func(3,4)
func(3)
func(a=8,b=9, c= 456)


def somefunc(a = 0, b = 0, s = "+"):
    return(a+b)
    if s == "-":
        return (a-b)
print(somefunc(10,1,"-"))

'''

import collections
from typing import Mapping
#def func(l):
#    l.reverse()
  
#l1 = [1,2,3]
#func(l1)
#print(l1)
'''
def count(s):
    return (dict(collections.Counter(s)))

print(count("Hello"))

def count(s):
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d[i] = 1
    return d

print(count("Hello"))
'''


# мой бред
'''
def calc(a,b,c):

    def minus (a,b):
        return (a-b)

    def plus (a,b):
        return (a+b)

    def mult (a,b):
        return (a*b)

    def div (a,b):
        return (a/b)


    if c == "+":
        return (a,b,)
    elif c == "-":
        return (minus)
    elif c == "*":
        return (mult)
    elif c == "/":
        return (div)

print(calc (5,3,"-"))
'''

def summ (a=0, b=0):
    return a + b
def sub (a=0, b=0):
    return a - b
def mult (a = 0, b = 0):
    return (a * b)
def div (a=0, b=0):
    return a/b
def calc (a=0, b=0, c = ""):
    if c == "+":
        return summ(a,b)
    elif c == "-":
        return sub(a,b)
    elif c == "*":
        return mult(a,b)
    elif c == "/":
        return div(a,b)

if __name__ == "__main__":       
    print(calc(1,2,"-"))







