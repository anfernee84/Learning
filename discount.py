def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = (price - price * discount)
        return(price)

    apply_discount()
    return price
print(discount_price(5, 0.9))



def get_fullname(first_name,last_name,middle_name = "" ):
  if middle_name == "":
    return str(first_name + " " + last_name)
  else:
    return str(first_name +  " " + middle_name + " " + last_name)

print(get_fullname("ivan", "ivanov"))

def format_string(string, length):
    if len(string) == length:
      return(string)
    else:
      return (" " *( (length - len(string)) // 2) + string)
print(format_string("vasya", 8))


def prepare_data(data):
    data.sort()
    data.pop(0)
    data.pop(-1)
    return(data)


print(prepare_data([4,5,6,3,2,1,7,6]))


def format_ingredients(items):
    s = ""
    end = items[-1]
    begin = items[0:-1]
    print (begin[-1])
    for i in begin:
        if i != (begin[-1]):
            s += i
            s += ", "
        else:
            s += i
    s += " и "
    s += end
#    print (type(s))
    return (s)

print(format_ingredients(["onion", "cucumber", "apple", "holly shit", "2 pieces of something"]))