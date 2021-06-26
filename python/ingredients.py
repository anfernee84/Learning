def format_ingredients(items):
    if len(items) == 1:
        return(str(items[0]))
    elif len(items) == 0:
        return ""
    else:
        s = ""
        end = items[-1]
        begin = items[0:-1]
        for i in begin:
            if i != (begin[-1]):
                s += i
                s += ", "
            else:
                s += i
        s += " и "
        s += end
    return (s)
print(format_ingredients(["onion", "cucumber", "apple", "holly shit", "2 pieces of something"]))

def format_ingredients(items):
    items = ', '.join(items)
    print (items)
    recipe = items[::-1].replace(","[::-1], " и"[::-1], 1)[::-1]
    return recipe
print(format_ingredients(["onion", "cucumber", "apple", "holly shit", "2 pieces of something"]))

