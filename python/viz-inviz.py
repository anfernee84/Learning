viz = 0
def func1():
    plusfive = viz + 5
    print(plusfive)
def func2():
    global viz
    viz = viz + 10
    return viz

func1()
func2()
print(viz)