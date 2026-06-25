import math

point_A = [-3, 4, -5]
point_B = [2, 0, -4]

def diff_3d(point_A, point_B):
    output = math.sqrt(abs((point_A[0] - point_B[0])**2) + abs((point_A[1] - point_B[1])**2) + abs((point_A[2] - point_B[2])**2))
    return output

print(diff_3d(point_A, point_B))