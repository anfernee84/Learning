def format_ingredients(items):
    sortarr = []
    if len(items) > 1:
        sortarr = ", ".join(items[:-1])
        sortarr += " и " + "".join(items[-1])
    elif len(items) == 1:
        sortarr = "".join(items[0])
    elif len(items) == 0:
        sortarr = ""
    return (sortarr)



words = ["rehbwf","wvevvev", "rvwrv"]
print (format_ingredients(words))