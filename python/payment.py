def amount_payment(payment):
    spisok = []
    sum = 0
    for p in payment:
        if p > 0:
            spisok.append(p)
    for s in spisok:
        sum = sum + s
    return(sum)

pay = [1,5,8,4,5,3]
print (amount_payment(pay))



def amount_payment(payment):
    spisok = payment.copy()
    sum = 0
    for s in spisok:
        sum = sum + s
    return(sum)

pay = [1,5,8,4,5,3]
print (amount_payment(pay))