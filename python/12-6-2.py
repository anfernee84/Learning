import base64


def encode_data_to_base64(data):
    retlist = []
    for i in data:
        message_bytes = i.encode("utf-8")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("utf-8")
        retlist.append(base64_message)
    return(retlist)
        



rint(encode_data_to_base64(['Andreiev:uyro18890D', 'Stivenson:oppjM13LL9e']))





# import base64

# message = "Hello world!"
# message_bytes = message.encode("utf-8")
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode("utf-8")

# print(base64_message)  # SGVsbG8gd29ybGQh