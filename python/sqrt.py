'''
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
def distance(x1, y1, x2, y2):
    return (((x2-x1)**2 + (y2-y1)**2) ** 0.5)
print (distance(x1, y1, x2, y2))
'''
'''
def distance():
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    return (((x2-x1)**2 + (y2-y1)**2) ** 0.5)

print (distance())
'''
'''
a = float(input())
n = int(input())
def power(a, n):
    if n == 0:
        return 1
    else:
        return a * power(a, n - 1)

print(power(a, n))
'''

def getTotal(n, total):
    print n
    if n == 0:  # base condition
        return total
    else:
        return getTotal(n-1, (total+(n)))
print getTotal(5, 0)