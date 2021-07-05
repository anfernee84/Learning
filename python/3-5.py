def sanitize_phone_number(phone):
    phone = phone.replace("+", "").replace("(","").replace(")", "").replace("-","").replace(" ", "")
    return(phone.strip())

print(sanitize_phone_number("   +38(050)929-81-65   "))