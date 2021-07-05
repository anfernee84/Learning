# print('dec: {:d} hex: {:x} bin: {:b}'.format(15, 15, 15))  # dec: 15 hex: f bin: 1111
# print('pi: {:0.4}'.format(3.1415))  # pi: 3.14
# print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))  # "1" "+2" "-3" " 4"
# print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))  # |left      |**center**|     right|


def formatted_numbers():
    
    num_list = []
    num_list.append("|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary"))
    for i in range(0,16):
        s = "|{:<10d}|{:^10x}|{:>10b}|".format(i,i,i)
        num_list.append(s)
    return(num_list)
        
print(formatted_numbers())




