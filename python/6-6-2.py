def get_recipe(path, search_id):

    with open(path, 'r') as fh:
        strings = fh.readlines()
        result = {}
        for st in strings:
            if search_id in st:
                id = st.split(",")[0]
                name = st.split(",")[1]
                ingredients = st.split(",")[2:]
                result = {"id":id, "name":name, "ingredients":[i.strip() for i in ingredients[:]]}
                return (result)
       
            elif not str:
                break


print (get_recipe('test.txt', "60b90c2e13067a15887e1ae3"))


