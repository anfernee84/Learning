def total (initial =5, *numbers, extra_number):
    count = initial
    for i in numbers:
        count = count+i
    count = count + extra_number
    print(count)
total(10, 1, 2, 3, extra_number=50)
