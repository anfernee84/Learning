result = None
operand = None
operator = None
wait_for_number = True
while True:
    result = input("Enter first digit: ")
    try:
        result = int(result)
    except ValueError or TypeError:
        print (f"{result} is not a digit")
    else:
        break
while True:
        operator = str(input("Enter an operator (+,-,*,/): "))    
        if operator == ("+"):
#                result = input("Enter next digit: ")
                try:
                    result = result + int(input("Enter next digit: "))
                except ValueError or TypeError:
                        print (f"{result} is not a digit")
                        continue
                else:
                    break    
        elif operator == ("-"):
            if result == None:
                result = operand - float (input("Enter second digit: "))
            else:
                result = result - float(input("Enter next digit: "))
        elif operator == ("*"):
            if result == None:
                result = operand * float (input("Enter second digit: "))
            else:
                result = result * float (input("Enter next digit: "))
        elif operator == ("/"):
            if result == None:
                result = operand / float (input("Enter second digit: "))
            else:
                result = result / float (input("Enter next digit: "))
        elif operator == ('='):
            print (f"Result: {result}")
        else:
            print ("Incorrect operator, try again")
        continue