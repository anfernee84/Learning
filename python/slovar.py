points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
def calculate_distance(coordinates):
    distance = []

    if len(coordinates) <= 1:
            return 0
    else:
        for i in range(len(coordinates)-1):
            (coordinates[i], coordinates [i+1]) # вот в этом моменте не совсем понимаю - что значит проверить их в points

    return sum(distance)
coordinates = [0, 1, 3, 2, 0, 2]
print(calculate_distance(coordinates))