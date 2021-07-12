def write_to_bin(path, user_info):

    with open(path, 'wb') as f:
        for i, j in user_info.items():
            s = i + ':' + j + '\n'
            f.write(s.encode('utf-8'))


    with open(path, 'rb') as filehandler:
        s = filehandler.readlines()
        l = []
        for i in s:
            l.append (i.decode('utf-8').rstrip('\r\n'))
        return l



print(write_to_bin("test.txt", {'Andreiev':'uyro18890D', 'Stivenson':'oppjM13LL9e'}))



