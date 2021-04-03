

def fibo(n):
    if n == 1:
        return 0
    elif n < 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)




def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)



if __name__ == '__main__':
    print(fibo(4))
    print(fibonacci(4))