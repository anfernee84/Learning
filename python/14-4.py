import sys


def parse_args():
    result = ""
    for arg in sys.argv[1:]:
            result = result + arg
            result = result + " "
    result = result[:-1]     
    print(result)
    
    return result
