#!/usr/bin/python3
from pathlib import Path
from sys import argv
from pprint import pprint

img = ('jpg', 'svg', 'png')
docs =  ('docx','pdf')


list_img=[]
list_docs=[]
list_unknown=[]

def check_ext(file):
 
    ext = file.split('.')[-1:][0]
    
    if ext in img:
        list_img.append(file)

    if ext in docs:
        list_docs.append(file)

    elif ext not in img + docs:
        list_unknown.append(ext)

def search(path):
    try:
        p = Path(path)
        for x in p.iterdir():
            if not x.is_dir():
                check_ext(str(x.absolute()))
            else:    
                search(x.absolute())
    except PermissionError:
        print('error 13')

search(argv[1])

pprint(('IMG', list_img))
pprint(('DOCS', list_docs))
pprint(('UNKNOWN',set(list_unknown)))
