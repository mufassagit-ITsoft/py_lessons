point_A = [1, 2, 3]
point_B = [-4, -5, 6]

# Formula: dist = (abs((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2))^1/2
dist = (abs((point_A[0] - point_B[0])**2 + (point_A[1] - point_B[1])**2 + (point_A[2] - point_B[2])**2))**(1/2)

print(f"dist = {dist}")

# use of pow(c,e)
dist2 = pow(abs(pow((point_A[0] - point_B[0]),2) + pow((point_A[1] - point_B[1]),2) + pow((point_A[2] - point_B[2]),2)),(1/2))
print(f"dist = {dist2}")

import math

dist3 = pow((point_A[0] - point_B[0]),2) + pow((point_A[1] - point_B[1]),2) + pow((point_A[2] - point_B[2]),2)
result = math.sqrt(dist3)
print(f"dist = {result}")

