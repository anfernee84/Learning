import re
map = {ord('з'): 'z', ord('ю'): 'u'}
translated = 'зю'.translate(map)
print(translated) # zu

symbols = "0123456789ABCDEF"
code = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]


MAP = {}

print(zip(symbols,code))

for s, c in zip (symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

result = "34 5D 56 AC". translate(MAP)
print(result)




string = "Bohr founded the Institute of Theoretical Physics at the University of Copenhagen, now known as the Niels Bohr Institute, which opened in 1920"
pattern = r"\d+"
result = re.search(pattern, string)
#print(result.span())
#print(result.group())
#print(result.string)

result = re.findall(pattern, string)
print(result)
print(len(result))

result = re.findall(r'\d', string)
print(result)
print(len(result))

