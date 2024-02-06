import math

def euclidean_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same dimension")
    
    distance = 0
    for i in range(len(vector1)):
        distance += (vector1[i] - vector2[i]) ** 2

    return math.sqrt(distance)

def manhattan_distance(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must be of the same dimension")

    distance = 0
    for i in range(len(vector1)):
        distance += (vector1[i] - vector2[i])

    return distance if distance >= 0 else -distance

vector_a = [1, 2, 3]
vector_b = [4, 5, 6]

euclidean_dist = euclidean_distance(vector_a, vector_b)
manhattan_dist = manhattan_distance(vector_a, vector_b)

print("Euclidean Distance:", euclidean_dist)
print("Manhattan Distance:", manhattan_dist)
