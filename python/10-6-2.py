def save_credentials_users(path, users_info):
    with open(path, 'wb') as f:
        for i, j in users_info.items():
            s = i + ':' + j + '\n'
            f.write(s.encode('utf-8'))
            



print((save_credentials_users("test.txt", {'andry':'uyro18890D', 'steve':'oppjM13LL9e'})))
