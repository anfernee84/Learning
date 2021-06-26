def amount_payment(payment):
    sum = 0
    for i in payment:
        if i > 0: 
            sum+=i
    return(sum) 

print(amount_payment([4,6,-4,7]))