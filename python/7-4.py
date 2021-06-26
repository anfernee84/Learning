points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
def calculate_distance(coordinates):
    distance = 0
    step = []
    if len(coordinates) > 1:
        for i in coordinates[:-1]:
            step.append(sorted(coordinates[0:2]))
            coordinates = coordinates[1:]
    for i in step:
        i = tuple(i)
        if tuple(i) in points.keys():
            distance += points.get(i)
    return(distance)        

print(calculate_distance([0, 1, 3, 2, 0, 2]))



