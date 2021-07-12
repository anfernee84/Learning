def encode_password(password):
    return [hex(i) for i in password.encode()]




print(encode_password("!q2w3e4r"))