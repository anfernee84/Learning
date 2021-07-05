articles_dict = [
    {
        "title": "Minim voluptate eu aliqua duis pariatur cupidatat voluptate.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Dolore Lorem aliquip est labore elit labore ex consequat ad occaecat duis.",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "Aliqua minim amet ut pariatur et occaecat esse qui commodo ut duis sunt elit.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "Irure reprehenderit aliquip officia quis occaecat aute mollit laborum ullamco laboris Lorem commodo.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    newlist = []
    for item in articles_dict:
        for i,j in item.items():
            if type(j) == int:
                continue
            elif j.find(key) != -1:
                newlist.append(item)
    return(newlist) 
        


print(find_articles("qui"))
            
        
        
            
        
    