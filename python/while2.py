total = 100

while total > 0:
    n = int(input())
    if n < total:
        total = total - n
    else:
        print("Ресурс исчерпан", end='\n') 